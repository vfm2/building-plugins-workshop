#!/usr/bin/env python3
"""Focused, offline checks for this workshop, not a general schema validator."""

import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = "https://agent-plugins.org/schemas/1.0.0/"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class WorkshopChecks(unittest.TestCase):
    def test_manifest(self):
        manifest = json.loads((ROOT / "plugin.json").read_text())
        self.assertEqual(
            set(manifest),
            {"$schema", "name", "version", "description", "repository", "license", "keywords"},
        )
        self.assertEqual(manifest["$schema"], SCHEMAS + "plugin.schema.json")
        self.assertRegex(manifest["name"], r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
        self.assertLessEqual(len(manifest["name"]), 64)
        self.assertEqual(manifest["version"], "1.0.0")
        for field in ("description", "repository", "license"):
            self.assertIsInstance(manifest[field], str)
            self.assertTrue(manifest[field])
        self.assertIsInstance(manifest["keywords"], list)
        self.assertTrue(all(isinstance(word, str) for word in manifest["keywords"]))

    def test_portable_mcp(self):
        config = json.loads((ROOT / "mcp.json").read_text())
        self.assertEqual(config, {
            "$schema": SCHEMAS + "mcp.schema.json",
            "mcpServers": {
                "figma": {
                    "type": "streamable-http",
                    "url": "https://mcp.figma.com/mcp",
                }
            },
        })

    def test_marketplace(self):
        catalog = json.loads((ROOT / ".github/plugin/marketplace.json").read_text())
        manifest = json.loads((ROOT / "plugin.json").read_text())
        self.assertEqual(catalog["name"], "building-plugins-workshop")
        self.assertTrue(catalog["owner"]["name"])
        self.assertEqual(len(catalog["plugins"]), 1)
        plugin = catalog["plugins"][0]
        self.assertEqual(plugin["name"], manifest["name"])
        self.assertEqual(plugin["version"], manifest["version"])
        self.assertEqual((ROOT / plugin["source"]).resolve(), ROOT)

    def test_skill_and_optional_agent(self):
        skill = ROOT / "skills/web-design-guidelines/SKILL.md"
        text = skill.read_text()
        self.assertTrue(text.startswith("---\nname: web-design-guidelines\n"))
        self.assertRegex(text, r"\ndescription: [^\n]+\n---\n")
        for instruction in ("Figma", "fallback", "File:line", "320", "review-only"):
            self.assertIn(instruction, text)
        agent = ROOT / "com.github.copilot/agents/design-reviewer.agent.md"
        self.assertIn("web-design-guidelines", agent.read_text())
        self.assertFalse((ROOT / "agents").exists())
        self.assertFalse((ROOT / "hooks.json").exists())

    def test_rules(self):
        rules = ROOT / "com.github.copilot/rules/workshop-guardrails.md"
        text = rules.read_text()
        for instruction in ("Figma", "dependencies", "browser", "synthetic local brief"):
            self.assertIn(instruction, text)

    def test_local_markdown_links(self):
        paths = [ROOT / "README.md"]
        for directory in ("docs", "demo", "skills", "com.github.copilot"):
            paths.extend((ROOT / directory).rglob("*.md"))
        for path in paths:
            for target in re.findall(r"\[[^\]]+\]\(([^)\s]+)\)", path.read_text()):
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                with self.subTest(file=str(path.relative_to(ROOT)), target=target):
                    resolved = (path.parent / unquote(url.path)).resolve()
                    self.assertTrue(resolved.is_relative_to(ROOT), target)
                    self.assertTrue(resolved.exists(), target)

    def test_sample_behavior_and_layout_invariants(self):
        for name in ("index.html", "reference.html"):
            path = ROOT / "demo" / name
            text = path.read_text()
            page = Page(path)
            with self.subTest(file=name):
                self.assertIn(("html", {"lang": "en"}), page.tags)
                self.assertEqual(sum(tag == "h1" for tag, _ in page.tags), 1)
                inputs = [attrs for tag, attrs in page.tags if tag == "input"]
                self.assertEqual(len(inputs), 1)
                self.assertEqual(inputs[0]["id"], "email")
                self.assertEqual(inputs[0]["type"], "email")
                self.assertEqual(inputs[0]["autocomplete"], "email")
                self.assertIn("required", inputs[0])
                self.assertIn(("meta", {"name": "viewport", "content": "width=device-width, initial-scale=1"}), page.tags)
                self.assertIn("box-sizing: border-box", text)
                self.assertIn("max-width: 32rem", text)
                self.assertIn("event.preventDefault()", text)
                self.assertIn("role=\"status\"", text)
                self.assertNotRegex(text, r"https?://|\bfetch\s*\(|localStorage")
                self.assertFalse(any(tag == "form" and "action" in attrs for tag, attrs in page.tags))

    def test_prepared_result_repairs(self):
        path = ROOT / "demo/reference.html"
        page = Page(path)
        text = path.read_text()
        self.assertIn(("label", {"for": "email"}), page.tags)
        self.assertIn(("h2", {}), page.tags)
        self.assertNotIn(("h3", {}), page.tags)
        self.assertIn(":focus-visible", text)
        self.assertNotIn("outline: none", text)

    def test_timing_and_fallback_documentation(self):
        script = (ROOT / "docs/facilitator-script.md").read_text()
        for boundary in ("0:00-1:30", "3:15-5:00", "5:00-6:30", "14:00-15:00"):
            self.assertIn(boundary, script)
        guide = (ROOT / "docs/demo-guide.md").read_text()
        for required in ("not a live", "copilot --plugin-dir .", "publication", "Sign in"):
            self.assertIn(required, guide)


if __name__ == "__main__":
    unittest.main(verbosity=2)

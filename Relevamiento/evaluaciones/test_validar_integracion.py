"""Regression checks for the structural validator using disposable fixtures."""

from pathlib import Path
import tempfile
import unittest

from validar_integracion import validate


class IntegrationValidationTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="relevamiento-validator-")
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name)
        self.skills = []
        for owner, name in (
            ("Relevamiento", "relevamiento"),
            ("Presupuestos", "aftercode-presupuesto-integral"),
        ):
            for folder in ("skills", ".codex/skills"):
                skill = self.root / owner / folder / name
                (skill / "references").mkdir(parents=True)
                (skill / "SKILL.md").write_text(
                    "[Contract](references/traspaso-presupuestos.md)\n", encoding="utf-8"
                )
                (skill / "references/traspaso-presupuestos.md").write_text(
                    "# Shared contract\n", encoding="utf-8"
                )
                self.skills.append(skill)

    def test_valid_bundle(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_counterpart(self):
        (self.skills[0] / "extra.md").write_text("New reference\n", encoding="utf-8")
        self.assertTrue(validate(self.root))

    def test_changed_mirror(self):
        (self.skills[1] / "SKILL.md").write_text("Different entrypoint\n", encoding="utf-8")
        self.assertTrue(validate(self.root))

    def test_contract_drift_even_when_mirrors_match(self):
        for skill in self.skills[2:]:
            (skill / "references/traspaso-presupuestos.md").write_text(
                "# Other contract\n", encoding="utf-8"
            )
        self.assertTrue(validate(self.root))

    def test_broken_local_link(self):
        for skill in self.skills:
            (skill / "SKILL.md").write_text("[Missing](missing.md)\n", encoding="utf-8")
        self.assertTrue(validate(self.root))

    def test_external_and_anchor_links_not_local(self):
        for skill in self.skills:
            (skill / "SKILL.md").write_text(
                "[Remote](https://example.invalid/a) [Section](#section)\n", encoding="utf-8"
            )
        self.assertEqual(validate(self.root), [])


if __name__ == "__main__":
    unittest.main()

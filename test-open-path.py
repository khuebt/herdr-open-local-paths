import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("opener", Path(__file__).with_name("open-path.py"))
opener = importlib.util.module_from_spec(spec)
spec.loader.exec_module(opener)


class LocalPathTests(unittest.TestCase):
    def test_relative_links_use_clicked_pane_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "docs" / "plan.md"
            target.parent.mkdir()
            target.write_text("fixture")
            self.assertEqual(opener.local_path("docs/plan.md", directory), target)
            self.assertEqual(opener.local_path("docs/plan.md:12:3", directory), target)
            self.assertEqual(opener.local_path("docs", directory), target.parent)
            self.assertEqual(opener.local_path(target.as_uri()), target)
            self.assertIsNone(opener.local_path("docs/plan.md"))

    def test_empty_missing_and_remote_targets_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            for value in ("", "missing.md", "https://example.com", "file://remote/etc/passwd", "bad\npath"):
                with self.subTest(value=value):
                    self.assertIsNone(opener.local_path(value, directory))


if __name__ == "__main__":
    unittest.main()

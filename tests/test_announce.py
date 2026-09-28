"""The eval announcement is built from the generated reports the lock selects."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('announce_eval', ROOT/'scripts/announce_eval.py')
announce = importlib.util.module_from_spec(spec)
spec.loader.exec_module(announce)


class AnnounceTests(unittest.TestCase):
    def test_caption_summarizes_the_selected_matrix(self):
        matrix = json.loads((ROOT/'reports.lock.json').read_text())['matrix']
        text = announce.caption(ROOT, 'https://example.test/blob/abc')
        self.assertTrue(text.startswith('<b>Eval'))
        self.assertIn('client decisions agree with the draft', text)
        self.assertIn(f'href="https://example.test/blob/abc/{matrix}/README.md"', text)
        self.assertNotIn('**', text)

    def test_markdown_becomes_telegram_html(self):
        self.assertEqual(announce.inline('**3 of 4** agree in [Reth](clients/reth.md) & <b>'),
                         '<b>3 of 4</b> agree in Reth &amp; &lt;b&gt;')
        self.assertEqual(announce.paragraph('# T\n\n## Verdict changes\n\nNo captured verdict changed.\n', '## Verdict changes'),
                         'No captured verdict changed.')


if __name__ == '__main__':
    unittest.main()

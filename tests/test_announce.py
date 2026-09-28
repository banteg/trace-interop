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
    def test_caption_scores_every_charted_client(self):
        matrix = json.loads((ROOT/'reports.lock.json').read_text())['matrix']
        progress = json.loads((ROOT/'reports/progress.json').read_text())
        text = announce.caption(ROOT, 'https://example.test/blob/abc')
        self.assertTrue(text.startswith(f'<b>Eval {Path(matrix).parent.name}</b>'))
        dev = text.split('\nDev: ', 1)[1].split('\n', 1)[0]
        self.assertEqual([part.split()[0] for part in dev.split(' · ')], [c['name'] for c in progress['clients']])
        self.assertIn(f'href="https://example.test/blob/abc/{matrix}/README.md"', text)

    def test_scores_show_gains_and_losses(self):
        self.assertEqual(announce.score(20), '20')
        self.assertEqual(announce.score(20, gained=0, lost=0, build=['2.7.0']), '20')
        self.assertEqual(announce.score(23, gained=7), '23 (+7)')
        self.assertEqual(announce.score(9, gained=2, lost=1), '9 (+2 −1)')


if __name__ == '__main__':
    unittest.main()

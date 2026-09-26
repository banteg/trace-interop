"""The decision tables quote the pinned draft and find its known conflict and gaps."""
import copy
import unittest

from trace_interop.cli import ROOT, read
from trace_interop.tables import FILTERS, FRAMES, blocks, evaluate, report, schema_forms, verify

SPEC = read(ROOT/'spec/trace-openrpc.json')


def findings(table, kind):
    return [(r['cell'], r[kind]) for r in evaluate(table) if r[kind]]


class Tables(unittest.TestCase):
    def test_quotes_occur_in_the_pinned_draft(self):
        report(SPEC)
        reworded = copy.deepcopy(SPEC)
        for m in reworded['methods']:
            m['description'] = m['description'].replace('mode union matches either populated list', 'mode union matches any list')
            m['params'][0]['schema'].pop('description', None)
        with self.assertRaisesRegex(ValueError, 'mode union matches either populated list'):
            verify(reworded, [FILTERS])

    def test_zero_value_precompile_at_the_depth_limit_conflicts(self):
        conflicts = findings(FRAMES, 'conflicts')
        self.assertTrue(conflicts)
        for cell, attributes in conflicts:
            self.assertEqual((cell['target'], cell['value'], cell['outcome']), ('precompile', 'zero', 'precheck depth'))
            self.assertEqual(set(attributes['emitted']), {True, False})

    def test_ordinary_frame_emission_is_unstated(self):
        gaps = findings(FRAMES, 'gaps')
        self.assertTrue(gaps)
        self.assertTrue(all(c['target'] == 'account' and c['outcome'] in ('success', 'revert', 'halt') and a == ['emitted'] for c, a in gaps))

    def test_address_filtering_is_decided_everywhere(self):
        self.assertEqual(findings(FILTERS, 'conflicts'), [])
        self.assertEqual(findings(FILTERS, 'gaps'), [])

    def test_block_selection_gaps(self):
        gaps = {(c['method'], c['selector'], c['history']) for c, _ in findings(blocks(SPEC), 'gaps')}
        self.assertIn(('trace_callMany', 'unknown hash', 'available'), gaps)
        self.assertIn(('trace_call', 'non-canonical hash', 'available'), gaps)
        self.assertIn(('trace_filter', 'unresolvable safe', 'available'), gaps)
        self.assertNotIn(('trace_call', 'unknown hash', 'available'), gaps)
        self.assertEqual(findings(blocks(SPEC), 'conflicts'), [])

    def test_schema_forms(self):
        self.assertFalse({'hash', 'pending', 'omitted'} & schema_forms(SPEC, 'trace_block'))
        self.assertTrue({'hash', 'pending', 'omitted'} <= schema_forms(SPEC, 'trace_call'))
        self.assertIn('omitted', schema_forms(SPEC, 'trace_filter'))
        self.assertNotIn('pending', schema_forms(SPEC, 'trace_filter'))


if __name__ == '__main__':
    unittest.main()

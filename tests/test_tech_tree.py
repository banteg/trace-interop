"""The tech tree page takes its states and numbers from the tracker; tree.toml only lays it out."""
import importlib.util
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_tech_tree', ROOT/'scripts/build_tech_tree.py')
tech_tree = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tech_tree)

GETH = 'https://github.com/ethereum/go-ethereum/pull/1'
SPEC = 'https://github.com/ethereum/execution-apis/pull/2'
SETTLED = {'fix': 0, 'converged': 0, 'review': 0, 'policy': 0, 'unmeasured': 2}


def node(id, cell, **binding):
    return {'id': id, 'title': id.title(), 'sub': 'v{version}', 'icon': 'gear', 'cell': cell, 'category': 'dev',
            'url': 'https://example.test', 'text': 'Text.'} | binding


def tree():
    return {'layout': {'gutters': [40] * 6}, 'era': [], 'advisor': {}, 'actor': [], 'contributor': [], 'repo': [], 'step': [],
            'node': [node('lib', [0, 0], repos=['org/lib']),
                     node('dev', [1, 0], requires=['lib'], client='x', build='development'),
                     node('rel', [2, 0], requires=['dev'], client='x', build='release'),
                     node('geth', [1, 1], critical=True, pr=GETH),
                     node('fixtures', [2, 1], critical=True, requires=['geth'], done_with='spec', locked_until=['geth'], label='generating'),
                     node('spec', [3, 1], critical=True, requires=['fixtures'], pr=SPEC, locked_until=['fixtures'], progress='converged'),
                     node('hive', [4, 1], critical=True, requires=['spec', 'rel'], status='active', locked_until=['spec'])]}


def tracker(dev=30, release=30, counts=SETTLED, lib=('merged',), geth='open', spec='open'):
    pr = lambda url, state: {'url': url, 'state': state, 'draft': state == 'open', 'merged_at': None}
    client = {'client': 'x', 'name': 'X', 'counted': True, 'counts': counts, 'prs': {'merged': 5, 'open': 1},
              'builds': {'development': {'agree': dev, 'build': ['2.0.0-dev · aaaa']},
                         'release': {'agree': release, 'build': ['1.9.0 · bbbb']}}}
    return {'progress': {'decisions': 33, 'clients': [client]},
            'fixes': {'checked_at': '2026-10-03',
                      'prs': [pr(f'https://github.com/org/lib/pull/{i}', state) for i, state in enumerate(lib)]
                             + [pr(GETH, geth), pr(SPEC, spec)]},
            'status': {'H01': {'policy': 'converged'}, 'H02': {'policy': 'under_review'}},
            'captured': '2026-10-02'}


def states(data):
    return {n['id']: (n['status'], n['label']) for n in data['nodes']}


class TechTreeTests(unittest.TestCase):
    def test_pr_totals_cover_every_tracked_pr_except_closed(self):
        totals = tech_tree.build(tree(), **tracker(lib=('merged', 'open', 'closed')))['totals']
        self.assertEqual((totals['merged'], totals['open']), (1, 3))

    def test_repository_tree_is_a_laid_out_dag(self):
        data = tech_tree.build(**tech_tree.load())
        nodes = {n['id']: n for n in data['nodes']}
        self.assertEqual(len(nodes), len(data['nodes']))
        cells = [(n['col'], n['row'] + i) for n in data['nodes'] for i in range(n['span'])]
        self.assertEqual(len(cells), len(set(cells)), 'two nodes share a cell')
        self.assertGreaterEqual(len(data['layout']['gutters']), max(n['col'] for n in data['nodes']))
        actors = {a['id'] for a in data['actors']}
        for n in data['nodes']:
            self.assertTrue(set(n['requires']) <= nodes.keys(), n['id'])
            self.assertTrue(n['actor'] is None or n['actor'] in actors, n['id'])
            self.assertTrue(all(nodes[r]['col'] <= n['col'] for r in n['requires']), f'{n["id"]} requires a later column')
        for step in data['steps']:
            self.assertTrue(set(step['nodes']) <= nodes.keys(), step['title'])

        def visit(id, path=()):
            self.assertNotIn(id, path, f'cycle through {id}')
            for r in nodes[id]['requires']:
                visit(r, path + (id,))
        for id in nodes:
            visit(id)

    def test_libraries_are_done_once_no_pr_is_open(self):
        self.assertEqual(states(tech_tree.build(tree(), **tracker(lib=('merged', 'open', 'closed'))))['lib'], ('active', None))
        lib = next(n for n in tech_tree.build(tree(), **tracker(lib=('merged', 'closed')))['nodes'] if n['id'] == 'lib')
        self.assertEqual((lib['status'], lib['prs']), ('done', {'merged': 1, 'open': 0}))

    def test_a_release_is_done_once_it_matches_a_settled_dev_build(self):
        unsettled = states(tech_tree.build(tree(), **tracker(counts=SETTLED | {'converged': 1})))
        self.assertEqual((unsettled['dev'][0], unsettled['rel'][0]), ('active', 'active'))
        self.assertEqual(states(tech_tree.build(tree(), **tracker(release=28)))['rel'][0], 'active')
        data = tech_tree.build(tree(), **tracker())
        self.assertEqual((states(data)['dev'][0], states(data)['rel'][0]), ('done', 'done'))
        dev = next(n for n in data['nodes'] if n['id'] == 'dev')
        self.assertEqual((dev['sub'], dev['progress']), ('v2.0.0-dev', [30, 33, 'decisions agree']))

    def test_gates_open_as_their_prs_merge(self):
        draft = tech_tree.build(tree(), **tracker())
        self.assertEqual(states(draft)['geth'], ('active', 'draft PR'))
        self.assertEqual(states(draft)['fixtures'], ('locked', 'waits on Geth'))
        self.assertEqual(states(draft)['spec'], ('locked', 'waits on Fixtures'))
        self.assertEqual(states(draft)['hive'], ('locked', 'waits on Spec'))
        self.assertEqual(draft['researching'], 'geth')

        geth = tech_tree.build(tree(), **tracker(geth='merged'))
        self.assertEqual(states(geth)['fixtures'], ('active', 'generating'))
        self.assertEqual(geth['researching'], 'fixtures')

        merged = tech_tree.build(tree(), **tracker(geth='merged', spec='merged'))
        self.assertEqual({id: states(merged)[id][0] for id in ('fixtures', 'spec', 'hive')},
                         {'fixtures': 'done', 'spec': 'done', 'hive': 'active'})
        self.assertEqual(states(merged)['spec'][1], '1/33 converged')
        self.assertEqual(merged['researching'], 'hive')

    def test_page_embeds_the_data_once(self):
        template = (tech_tree.SITE/'index.html').read_text()
        self.assertEqual(template.count(tech_tree.PLACEHOLDER), 1)
        data = tech_tree.build(tree(), **tracker()) | {'nodes': [{'text': 'closes </script> early'}]}
        page = tech_tree.render(data, template)
        payload = re.search(r'<script id="tree-data" type="application/json">(.*?)</script>', page, re.DOTALL).group(1)
        self.assertEqual(json.loads(payload), data)


if __name__ == '__main__':
    unittest.main()

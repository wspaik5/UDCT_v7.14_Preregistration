#!/usr/bin/env python3
"""Validate protocol metadata and grid. Does NOT calculate any OM DF."""
import json,csv,itertools,pathlib
root=pathlib.Path(__file__).resolve().parent
p=json.loads((root/'PROTOCOL.json').read_text())
with (root/'PRESPECIFIED_GRID.csv').open(newline='') as f: rows=list(csv.DictReader(f))
expected={(float(a),float(b),float(c)) for a,b,c in itertools.product(p['p'],p['r_a_over_a'],p['energy_label_r_over_a'])}
actual={(float(r['p']),float(r['r_a_over_a']),float(r['energy_label_r_over_a'])) for r in rows}
assert len(rows)==p['n_points']==len(expected)==len(actual)==20
assert expected==actual
assert all(r['status']=='PLANNED_NOT_EXECUTED' for r in rows)
assert p['no_results_run'] is True
print('PASS: 20 unique planned grid points; no DF calculations executed.')

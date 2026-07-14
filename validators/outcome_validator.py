\"\"\"
Outcome Validator - Validates Desired Outcome statements.

Checks:
- Direction is valid (increase, decrease, eliminate, maintain, achieve)
- Object is specific (not vague)
- Metric is measurable
- No fuzzy language (easier, better, etc.)
- Solution-independent
\"\"\"

import json, sys, re

VAGUE_WORDS = [r'\beasier\b', r'\bbetter\b', r'\bmore convenient\b',
               r'\bimproved\b', r'\bfaster\b', r'\buser-friendly\b']


def validate_outcome(outcome):
    issues = []
    valid_directions = ['increase', 'decrease', 'eliminate', 'maintain', 'achieve']
    direction = outcome.get('direction', '').lower()
    if direction not in valid_directions:
        issues.append(f'Invalid direction: {direction}')

    obj = outcome.get('object', '')
    if len(obj) < 10:
        issues.append('Object too vague')

    metric = outcome.get('metric', '')
    if len(metric) < 10:
        issues.append('Metric not specific enough')

    full = outcome.get('full_statement', '')
    for pattern in VAGUE_WORDS:
        if re.search(pattern, full.lower()):
            word = re.search(pattern, full.lower()).group()
            issues.append(f'Fuzzy language detected: {word}')
            break

    if not outcome.get('evidence_ref'):
        issues.append('No evidence reference')

    return {'pass': len(issues) == 0, 'issues': issues,
            'quality': max(0, 1.0 - len(issues) * 0.25)}


def main():
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.load(open(sys.argv[1]))
    outcomes = data if isinstance(data, list) else data.get('outcomes', [data])
    results = [validate_outcome(o) for o in outcomes]
    for i, r in enumerate(results):
        status = 'PASS' if r['pass'] else 'FAIL'
        print(f'Outcome {i}: {status} (quality: {r.get("quality", 0):.1f})')
        [print(f'  - {x}') for x in r['issues']]
    return 0 if all(r['pass'] for r in results) else 1


if __name__ == '__main__':
    sys.exit(main())

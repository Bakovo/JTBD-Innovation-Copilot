\"\"\"
Need Validator - Validates need classification.

Checks:
- Need is categorized as Pain or Benefit with correct subcategory
- Evidence supports the need
- Intensity is specified
- Need is not a solution in disguise
\"\"\"

import json, sys, re

SOLUTION_PATTERNS = [r'\b(app|feature|button|click|interface|function)\b',
                     r'\bshould have\b', r'\badd a\b', r'\bmake it\b']


def validate_need(need):
    issues = []
    valid_categories = ['pain', 'benefit']
    valid_subcategories = ['barrier', 'risk', 'negative_consequence',
                           'required_benefit', 'expected_benefit',
                           'desired_benefit', 'unexpected_benefit']

    cat = need.get('category', '').lower()
    if cat not in valid_categories:
        issues.append(f'Invalid category: {cat}')
    sub = need.get('subcategory', '').lower()
    if sub not in valid_subcategories:
        issues.append(f'Invalid subcategory: {sub}')
    if cat == 'pain' and sub not in ['barrier', 'risk', 'negative_consequence']:
        issues.append('Subcategory mismatch for pain category')
    if cat == 'benefit' and sub not in ['required_benefit', 'expected_benefit',
                                        'desired_benefit', 'unexpected_benefit']:
        issues.append('Subcategory mismatch for benefit category')

    statement = need.get('need_statement', '')
    for pattern in SOLUTION_PATTERNS:
        if re.search(pattern, statement.lower()):
            issues.append('Need contains solution language')
            break

    if 'intensity' not in need or need.get('intensity') not in ['low', 'medium', 'high']:
        issues.append('Missing or invalid intensity')

    if not need.get('evidence_sources'):
        issues.append('No evidence sources')

    return {'pass': len(issues) == 0, 'issues': issues}


def main():
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.load(open(sys.argv[1]))
    needs = data if isinstance(data, list) else data.get('needs', [data])
    results = [validate_need(n) for n in needs]
    for i, r in enumerate(results):
        status = 'PASS' if r['pass'] else 'FAIL'
        print(f'Need {i}: {status}'); [print(f'  - {x}') for x in r['issues']]
    return 0 if all(r['pass'] for r in results) else 1


if __name__ == '__main__':
    sys.exit(main())

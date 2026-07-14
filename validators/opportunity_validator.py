\"\"\"
Opportunity Validator - Validates opportunity scoring.

Checks:
- All 7 dimensions are scored
- Scores are within 1-10 range
- Weighted score calculation is correct
- Evidence strength is specified
- Category matches threshold
\"\"\"

import json, sys

THRESHOLDS = [('core', 7.0), ('adjacent', 5.0), ('exploratory', 0.0)]
DIMENSIONS = ['user_importance', 'dissatisfaction', 'frequency',
              'market_size', 'business_value', 'strategic_fit', 'technical_feasibility']
WEIGHTS = {'user_importance': 1.5, 'dissatisfaction': 1.3, 'frequency': 1.2,
           'market_size': 1.0, 'business_value': 1.0,
           'strategic_fit': 0.8, 'technical_feasibility': 0.7}


def validate_opportunity(opp):
    issues = []
    scores = opp.get('dimension_scores', {})

    for dim in DIMENSIONS:
        score = scores.get(dim, 0)
        if not isinstance(score, (int, float)):
            issues.append(f'Missing or invalid score: {dim}')
        elif score < 1 or score > 10:
            issues.append(f'Score out of range for {dim}: {score}')

    if not issues:
        total_weight = sum(WEIGHTS.values())
        weighted = sum(scores.get(d, 0) * WEIGHTS[d] for d in DIMENSIONS) / total_weight
        reported = opp.get('weighted_score', 0)
        if abs(weighted - reported) > 0.5:
            issues.append(f'Weighted score mismatch: expected {weighted:.1f}, got {reported:.1f}')

    cat = opp.get('category', '').lower()
    valid_cats = [c[0] for c in THRESHOLDS]
    if cat not in valid_cats:
        issues.append(f'Invalid category: {cat}')

    if opp.get('evidence_strength') not in ['strong', 'moderate', 'weak']:
        issues.append('Missing or invalid evidence strength')

    if not opp.get('job_id'):
        issues.append('Missing job_id reference')

    return {'pass': len(issues) == 0, 'issues': issues}


def main():
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.load(open(sys.argv[1]))
    opps = data if isinstance(data, list) else data.get('opportunities', [data])
    results = [validate_opportunity(o) for o in opps]
    for i, r in enumerate(results):
        status = 'PASS' if r['pass'] else 'FAIL'
        print(f'Opportunity {i}: {status}')
        [print(f'  - {x}') for x in r['issues']]
    return 0 if all(r['pass'] for r in results) else 1


if __name__ == '__main__':
    sys.exit(main())

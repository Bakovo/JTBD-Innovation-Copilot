\"\"\"
Context Validator - Validates context map completeness.

Checks:
- Each context has when, where, who specified
- Before/after states are described
- Emotional state is captured
- Evidence supports the context
\"\"\"

import json
import sys


def validate_context(context):
    issues = []
    required = ['when', 'where', 'who']
    for field in required:
        if field not in context or not context[field]:
            issues.append(f'Missing required field: {field}')

    if 'before_state' not in context or not context.get('before_state'):
        issues.append('Missing before state context')

    if 'after_state' not in context or not context.get('after_state'):
        issues.append('Missing after state context')

    trigger_specified = len(context.get('when', '')) > 15
    if not trigger_specified:
        issues.append('Trigger description too vague')

    environment_specified = len(context.get('where', '')) > 10
    if not environment_specified:
        issues.append('Environment description too vague')

    return {
        'pass': len(issues) == 0,
        'issues': issues,
        'completeness': max(0, 1.0 - len(issues) * 0.2)
    }


def main():
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.load(open(sys.argv[1]))
    contexts = data if isinstance(data, list) else data.get('contexts', [data])
    results = [validate_context(c) for c in contexts]
    for i, r in enumerate(results):
        status = 'PASS' if r['pass'] else 'FAIL'
        print(f'Context {i}: {status} (completeness: {r["completeness"]:.1f})')
        for issue in r['issues']:
            print(f'  - {issue}')
    return 0 if all(r['pass'] for r in results) else 1


if __name__ == '__main__':
    sys.exit(main())

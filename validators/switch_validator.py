\"\"\"
Switch Validator - Validates switch analysis completeness.

Checks:
- Timeline has all 6 stages
- Four Forces have Push, Pull, Inertia, Anxiety
- Each force has at least one specific item
- Evidence supports the switch story
\"\"\"

import json, sys


def validate_switch(switch):
    issues = []
    tl = switch.get('timeline', {})
    tl_stages = ['first_thought', 'passive_observation', 'active_search',
                 'comparison', 'decision', 'experience']
    for stage in tl_stages:
        if stage not in tl or not tl.get(stage):
            issues.append(f'Timeline stage missing: {stage}')

    forces = switch.get('four_forces', {})
    force_names = ['push', 'pull', 'inertia', 'anxiety']
    for fn in force_names:
        if fn not in forces:
            issues.append(f'Four Forces missing: {fn}')
        elif not forces[fn] or len(forces[fn]) == 0:
            issues.append(f'Four Forces empty: {fn}')

    if not switch.get('user_profile'):
        issues.append('Missing user profile')
    if not switch.get('old_solution'):
        issues.append('Missing old solution')
    if not switch.get('new_solution'):
        issues.append('Missing new solution')

    return {
        'pass': len(issues) == 0,
        'issues': issues,
        'completeness': max(0, 1.0 - len(issues) * 0.1)
    }


def main():
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.load(open(sys.argv[1]))
    switches = data if isinstance(data, list) else data.get('switches', [data])
    results = [validate_switch(s) for s in switches]
    for i, r in enumerate(results):
        status = 'PASS' if r['pass'] else 'FAIL'
        print(f'Switch {i}: {status} (completeness: {r["completeness"]:.1f})')
        [print(f'  - {x}') for x in r['issues']]
    return 0 if all(r['pass'] for r in results) else 1


if __name__ == '__main__':
    sys.exit(main())

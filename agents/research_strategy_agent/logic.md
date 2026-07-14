# Research Strategy Logic

## Goal Detection Heuristics

### Keyword Clusters

Need Discovery: "understand", "why", "frustration", "pain point", "need", "job", "goal"
Competitive: "competitor", "alternative", "versus", "switch", "comparison", "market"
Validation: "concept", "idea", "prototype", "test", "would you", "interest"
Innovation: "new", "opportunity", "where to", "future", "trend", "disrupt"

### Workflow Path Selection

if goal == need_discovery and data contains switch stories -> switch_first
if goal == need_discovery and data contains steady-state -> job_first
if goal == competitive_analysis -> competition_first
if goal == concept_validation -> validation_first
if goal == innovation_exploration -> switch_first
if goal == mixed or unclear -> comprehensive

### Hypothesis Format

Good: "Users switch from solution A to B primarily because of [specific pain]"
Bad: "Why do users switch?"

Good: "Non-consumption in [scenario] is driven by [specific barrier]"
Bad: "There might be opportunities"

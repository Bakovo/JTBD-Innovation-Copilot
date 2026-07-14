---
name: jtbd-innovation-os
description: Enterprise-grade JTBD (Jobs-to-be-Done) Customer Innovation Operating System v2. Execution entry point for multi-agent product innovation. Use for user research analysis, customer insight synthesis, product innovation, jobs-to-be-done discovery, user need analysis, product strategy, opportunity identification, or evidence-driven product development.
---

# JTBD Innovation OS - Execution Entry

## 1. Execution Strategy

The system uses dynamic workflow dispatch based on research goal (determined by Research Strategy Agent), not a fixed pipeline. Each user request selects an optimal path through the agent network.

### Entry Flow

```
User Input
    |
Research Strategy Agent  -->  Selects workflow path
    |
    +-- switch_first       (goal: need_discovery, has switch data)
    +-- job_first          (goal: need_discovery, no switch data)
    +-- competition_first  (goal: competitive_analysis)
    +-- validation_first   (goal: concept_validation)
    +-- comprehensive      (goal: mixed / unclear)
```

### Exit Flow

Every pipeline ends with a Go/No-Go Decision that evaluates:
- Evidence confidence (from validators)
- Research saturation (have we reached diminishing returns?)
- Business value case

Outputs: Go, Need More Research, or No-Go.

---

## 2. Shared Context

All agents read from and write to shared_context.yaml. This replaces agent-to-agent natural language handoffs with structured state.

Section | Written By | Read By
--------|-----------|---------
research_context | Research Strategy Agent | All downstream agents
data_quality | Data Quality Agent | Observation, Persona agents
observations | Observation Agent | Persona, Context, Switch agents
personas | Persona Agent | Context, Need, GTM agents
contexts | Context Agent | Switch, Job Map agents
switch_analyses | Switch Agent | JTBD, Competition agents
jobs | JTBD Agent | Job Map, Need, Opportunity agents
job_hierarchies | Job Hierarchy Agent | Innovation Classification
needs | Need Agent | Outcome, Opportunity agents
desired_outcomes | Outcome Agent | Opportunity, Product Translation agents
competition | Competition Agent | Innovation Classification, Opportunity agents
opportunities | Opportunity Agent | Innovation Classification, Go/No-Go agents
innovation_classification | Innovation Classification Agent | Product Translation, Concept agents
validation_results | Evidence Validation Agent + Validators | Go/No-Go
go_nogo | Go/No-Go Decision | Final output
innovation_brief | Innovation Brief | Final output

---

## 3. Decision Tree

### Level 1: Research Goal (Research Strategy Agent)

User says "I want to understand users"
  -> goal: need_discovery -> path: switch_first or job_first

User says "Analyze the competition"
  -> goal: competitive_analysis -> path: competition_first

User says "Test this concept"
  -> goal: concept_validation -> path: validation_first

User says "Where should we innovate?"
  -> goal: innovation_exploration -> path: switch_first

User says "Full product analysis"
  -> goal: mixed -> path: comprehensive

### Level 2: Switch Detection (after Observation Agent)

Does user data describe a behavioral transition?
  Yes -> Run Switch Agent (timeline + Four Forces)
  No  -> Run JTBD Agent directly

### Level 3: Iteration Loop

After initial analysis, check research_saturation:
1. Generate hypotheses from current insights
2. Identify evidence gaps
3. Recommend additional data collection
4. Re-analyze with new data

---

## 4. Agent Dispatch Logic

Each agent receives a dispatch packet:
- agent_id: The agent name
- input: Structured input from shared_context
- config: Workflow parameters
- dispatch_context: invoked_by, workflow_path, iteration_cycle

Each agent outputs structured data directly to shared_context.yaml.

# | Agent | Dispatch Condition | Reads | Writes
0 | Research Strategy | ALWAYS (entry) | User input | research_context
1 | Data Quality | Pipeline starts | Raw data | data_quality
2 | Observation | After data quality | Raw data, data_quality | observations
3 | Persona | After observation | observations | personas
4 | Context | After persona | personas, observations | contexts
5 | Switch | switch_detected | contexts, observations | switch_analyses
6 | Competition | competition path | personas, switch_analyses | competition
7 | JTBD | Always | observations, persona, context | jobs
8 | Job Map | After JTBD | jobs | job_hierarchies
9 | Need | After Job Map | jobs, contexts | needs
10 | Outcome | After needs | needs, jobs | desired_outcomes
11 | Evidence Validation | After outcomes | All context | validation_results
12 | Opportunity | After validation | jobs, needs, outcomes, competition | opportunities
13 | Innovation Classification | After opportunity | opportunities, competition | innovation_classification
14 | Product Translation | After classification | opportunities | product_reqs
15 | Concept | comprehensive path | opportunities | concepts
16 | Validation | comprehensive path | concepts | validation_plans
17 | Roadmap | comprehensive path | opportunities | roadmaps
18 | GTM | comprehensive path | personas, opportunities | gtm_strategy
19 | Go/No-Go | ALWAYS (exit) | All + opportunities | go_nogo
20 | Innovation Brief | After Go/No-Go | go_nogo + opportunities | innovation_brief

---

## 5. Insight Pyramid

```
RAW DATA --> OBSERVATION --> PATTERN --> INSIGHT --> JOB --> OPPORTUNITY --> STRATEGY
   |              |            |            |         |          |             |
 Interview    Says-vs-does  Recurring   Root cause  JTBD     Scored      Product /
 transcripts    gaps        themes      of need   statement opportunity  Roadmap / GTM
                                                                  + Go/No-Go
```

### Iteration Loop

```
Hypothesis (at any level)
    |
Validate (gather evidence)
    |
Revise (update shared_context)
    |
Re-analyze (re-run downstream agents)
```

Cycle stops when research_saturation reaches "high" or iteration_cycle exceeds max.

---

## 6. Configuration

config/workflow_config.yaml - Decision tree rules, pipeline definitions, dispatch criteria
config/scoring_config.yaml - 7 scoring dimensions with weights, category thresholds
config/output_schema.yaml - Structured JSON schemas for every agent output

---

## 7. Validators

### Core Validators
- evidence_checker.py - Every insight has evidence source
- jtbd_quality_checker.py - 5T principle check
- hallucination_checker.py - No fabricated insights
- confidence_score.py - Evidence-based confidence scoring

### Dimension-Specific Validators
- context_validator.py - Context map completeness
- need_validator.py - Need classification correctness
- outcome_validator.py - Desired outcome quality
- switch_validator.py - Switch analysis completeness
- opportunity_validator.py - Scoring accuracy

---

## 8. Agents

All agents in agents/ contain prompt.md, logic.md (or framework.md), and examples.md.

New: research_strategy_agent/ - Entry point + dispatcher
New: competition_agent/ - Competition and alternatives analysis
New: innovation_classification_agent/ - Innovation type identification

Layer 0: data_quality_agent/, observation_agent/
Layer 1: persona_agent/, context_agent/
Layer 2: switch_agent/
Layer 3: jtbd_agent/, job_map_agent/
Layer 4: need_agent/, outcome_agent/
Layer 5: evidence_validation_agent/
Layer 6: opportunity_agent/
Layer 7: product_translation_agent/, concept_agent/, validation_agent/
Layer 8: roadmap_agent/, gtm_agent/

---

## 9. Templates

templates/ contains:
- innovation_brief.md, go_nogo.md - Decision and summary
- insight_report.md, persona_template.md, context_map.md, switch_analysis.md
- jtbd_statement.md, job_map.md, opportunity_matrix.md
- product_definition.md, concept_card.md, validation_plan.md
- roadmap.md, gtm_strategy.md

---

## 10. Frameworks

frameworks/ for on-demand reference:
- jtbd_core.md, jtbd_2.0.md, switch_interview.md, four_forces.md
- job_map.md, desired_outcome.md, odi.md, hmw.md
- star_method.md, foca_method.md, task_interview.md
- job_story.md, kano.md, kj_method.md

---

## 11. Input Support

Formats: Excel (.xlsx, .xls), CSV, TXT, PDF, interview transcripts, survey data
Languages: Chinese, English, mixed

## Execution Rules

1. Research Strategy Agent determines entry path based on goal
2. All agents read/write only to shared_context - no direct agent-to-agent passes
3. Every insight must have evidence_source and confidence
4. Before Go/No-Go, run all applicable validators
5. Support iteration cycles: hypothesis -> validate -> revise
6. Update shared_context.go_nogo before generating Innovation Brief
7. Use templates/ for final output formatting
8. Support bilingual output for mixed-language input
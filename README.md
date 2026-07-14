# AI Customer Innovation Copilot

An AI-native Customer Insight and Innovation Copilot that guides product teams from research planning to evidence-backed product decisions.

> People do not buy products. They hire products to make progress.

---

## Why This Exists

Product teams spend 70% of innovation effort on things users don't value. The root cause is not lack of data, but lack of structured thinking between user data and product decisions.

This copilot applies JTBD 2.0 methodology in a structured, multi-agent workflow that transforms raw user data into evidence-backed product decisions.

It does not replace product managers. It helps them think.

---

## Who It Is For

| Role | What It Does For You |
|------|---------------------|
| Product Manager | From user data to product requirements with traceable evidence |
| UX Researcher | Structured interview analysis, pattern detection, insight extraction |
| Innovation Lead | Opportunity identification, concept generation, innovation classification |
| Product Director | Evidence-backed prioritization, go/no-go decisions, strategic roadmap |
| Startup Founder | User need discovery, product-market fit validation, MVP definition |

---

## Use Cases

- **User Need Discovery**: Upload interview transcripts -> receive JTBD statements + prioritized opportunities
- **Churn Analysis**: Analyze exit interviews -> Four Forces analysis -> retention opportunity ranking
- **Competitive Analysis**: Map competitive landscape through JTBD lens -> identify non-consumption opportunities
- **Concept Validation**: Test product concept against user jobs -> receive validation plan + evidence gaps
- **Innovation Exploration**: Discover underserved jobs -> classify innovation type -> generate product concepts
- **Purchase Behavior**: Analyze decision journey -> switch timeline + trigger analysis -> GTM strategy

---

## Architecture

```
                  ┌─────────────────────────────────────────┐
                  │           AI Customer Innovation        │
                  │                Copilot                  │
                  │                                         │
  User Data ─────►│  Research Strategy ─► Mode Selection    │
                  │       │                                 │
                  │  ┌────┴────────┐                        │
                  │  │  Quick Mode │  (JTBD + Pain + Opp)  │
                  │  │Standard Mode│  (+ Persona + Context) │
                  │  │ Expert Mode │  (+ Competition + More)│
                  │  └────┬────────┘                        │
                  │       │                                 │
                  │  Pipeline Dispatch ─► Agent Execution   │
                  │       │                                 │
                  │  Human Checkpoints ◄─── User Review     │
                  │       │                                 │
                  │  Shared Context Memory                  │
                  │       │                                 │
                  │  Evidence Validation ─► Go/No-Go        │
                  │       │                                 │
                  │  Research Planning ─► Next Steps        │
                  └───────┴─────────────────────────────────┘
```

### The Insight Pyramid

```
RAW DATA ──► OBSERVATION ──► PATTERN ──► INSIGHT ──► JOB ──► OPPORTUNITY ──► STRATEGY
```

---

## Analysis Modes

| Mode | Outputs | Checkpoints | Time | When to Use |
|------|--------|-------------|------|-------------|
| Quick | JTBD + Pains + Opportunity Summary | None | 5-10 min | First look, early signal, quick check |
| Standard | Persona + Context + JTBD + Needs + Opportunity Ranking | 2 | 20-30 min | Product research, user study |
| Expert | Full + Competition + Conflicts + Roadmap + GTM + Research Plan | 5 | 60-90 min | Innovation project, strategic initiative |

Mode is auto-recommended based on your input. You can override.

---

## Human-in-the-loop Checkpoints

The copilot pauses at key stages for your review:

| Stage | Question You Answer |
|-------|-------------------|
| After Persona | Does this persona represent your users? |
| After Context | Are these scenarios accurate? |
| After JTBD | Do these statements match what you know? |
| After Opportunity | Do these priorities feel right? |
| After Concept | Are these concepts worth pursuing? |

At each checkpoint: confirm, modify, skip, or reanalyze.

---

## Quick Start

### Prerequisites

- Codex platform with Skill auto-discovery enabled
- User research data (interviews, surveys, reviews, transcripts)

### Usage

```text
Copy your user research data into Codex and describe what you need:

"Analyze these 12 interview transcripts and tell me what users need"
"Here's 500 survey responses - find innovation opportunities"
"Why are users churning? I have 8 exit interviews"
"Quick check on these app store reviews"
```

The copilot automatically:
1. Detects your goal and recommends analysis mode
2. Runs the appropriate pipeline
3. Pauses at checkpoints for your review
4. Delivers evidence-backed recommendations
5. Tells you what to research next

### Supported Input Formats

| Format | Example |
|--------|---------|
| Interview transcripts | Raw text, CN/EN |
| CSV / Excel | Survey results, structured feedback |
| PDF | Research reports |
| TXT | Reviews, comments, support tickets |

---

## Workflow Detail

```
Step 1  Research Strategy Agent ──► Detect goal + recommend mode
Step 2  Knowledge Memory ──► Check for historical insights
Step 3  Data Quality Agent ──► Assess data fitness
Step 4  Observation Agent ──► Surface says-vs-does gaps
Step 5  Persona Agent ──► Build user profiles
           ── Checkpoint: Review Persona ──
Step 6  Context Agent ──► Map user situations
           ── Checkpoint: Review Context (Expert only) ──
Step 7  Switch Agent or JTBD Agent ──► Extract jobs
           ── Checkpoint: Review JTBD ──
Step 8  Need Agent + Outcome Agent ──► Define needs
Step 9  Competition Agent ──► Map alternatives (Expert)
Step 10 Conflict Detection Agent ──► Find tensions (Expert)
Step 11 Evidence Validation ──► Check all insights
Step 12 Opportunity Agent ──► Score + rank
           ── Checkpoint: Review Opportunities (Expert) ──
Step 13 Innovation Classification ──► Type innovation (Expert)
Step 14 Product Translation + Concept ──► Generate concepts (Expert)
           ── Checkpoint: Review Concepts (Expert) ──
Step 15 Research Planning Agent ──► Recommend next steps
Step 16 Decision Copilot ──► Go / Need More Research / No-Go
```

---

## Outputs

| Output | Description | Available In |
|--------|-------------|-------------|
| Executive Summary | Top-line findings in 3 minutes | All modes |
| Persona Profile | User identity, behavior, motivation | Standard, Expert |
| Context Map | When, where, who, before, after | Standard, Expert |
| Switch Analysis | Timeline + Four Forces | Standard, Expert |
| JTBD Statements | When + I want to + So I can | All modes |
| Job Map | 8-step process map | Standard, Expert |
| Need Analysis | Pain/Benefit classification | All modes |
| Desired Outcomes | Measurable outcome statements | Standard, Expert |
| Competition Map | Direct + indirect + non-consumption | Expert |
| Conflict Map | User need tensions | Expert |
| Opportunity Ranking | Scored + categorized | All modes |
| Innovation Classification | Innovation type | Expert |
| Concept Cards | HMW-based product concepts | Expert |
| Validation Plan | Research to validate assumptions | Expert |
| Product Roadmap | 3-horizon plan | Expert |
| GTM Strategy | Positioning + channels + launch | Expert |
| Innovation Brief | One-page executive summary | Expert |
| Research Plan | Next steps for research team | Expert |

---

## Limitations

- This is an AI copilot, not a replacement for human researchers. All outputs should be validated with real users.
- The quality of insights depends on the quality and diversity of input data.
- JTBD analysis is most powerful with qualitative data (interviews, observations). Pure quantitative data (surveys alone) produces thinner insights.
- The copilot's domain knowledge is limited to what you provide. It does not have pre-existing industry expertise.
- Non-consumption analysis requires data from people who do NOT currently use solutions in your category.
- Knowledge Memory persists within a session. Cross-session memory is stored in shared_context but not yet in a persistent database.

---

## FAQ

**Q: Does this replace user interviews?**
A: No. It helps you analyze interview data more systematically. You still need to talk to real users.

**Q: What data do I need?**
A: At minimum, user interview transcripts or survey responses with open-ended questions. More data = better insights.

**Q: Can I use it with survey data only?**
A: Yes, but confidence will be lower. Qualitative data (interviews, observations) produces the richest JTBD insights.

**Q: How is this different from sentiment analysis or thematic analysis?**
A: Sentiment analysis tells you if users are happy or not. JTBD analysis tells you what progress users are trying to make and why current solutions fall short.

**Q: Does it support Chinese?**
A: Yes. Chinese, English, and mixed-language inputs are supported.

**Q: Can I customize the workflow?**
A: Yes. Analysis modes (Quick/Standard/Expert) let you control depth. Checkpoints let you pause at any stage.

---

## Project Structure

```
customer-innovation-copilot/
├── SKILL.md                       # Execution entry point
├── README.md                      # This file
├── execution/                     # Execution strategy documents
│   ├── strategy.md                # Execution strategy
│   ├── decision_tree.md           # Decision tree logic
│   └── dispatch.md                # Agent dispatch rules
├── context/                       # Shared context memory
│   └── shared_context.yaml        # Unified agent state
├── config/                        # Configuration files
│   ├── workflow_config.yaml       # Dynamic dispatch model
│   ├── analysis_modes.yaml        # Quick/Standard/Expert modes
│   ├── evidence_weights.yaml      # Source reliability weights
│   ├── checkpoints.yaml           # Human-in-the-loop points
│   ├── scoring_config.yaml        # Opportunity scoring params
│   └── output_schema.yaml         # Unified agent I/O schemas
├── agents/                        # Agent modules (20 agents)
│   ├── openai.yaml                # UI metadata
│   ├── research_strategy_agent/   # Entry point + dispatcher
│   ├── knowledge_memory_agent/    # Cross-session memory
│   ├── data_quality_agent/        # Data fitness assessment
│   ├── observation_agent/         # Says-vs-does gaps
│   ├── persona_agent/             # User profiles
│   ├── context_agent/             # Situation maps
│   ├── switch_agent/              # Timeline + Four Forces
│   ├── jtbd_agent/                # Job statement extraction
│   ├── job_map_agent/             # 8-step process mapping
│   ├── need_agent/                # Need classification
│   ├── outcome_agent/             # Desired outcome engineering
│   ├── competition_agent/         # Competitive landscape
│   ├── conflict_detection_agent/  # User need conflicts
│   ├── evidence_validation_agent/ # Evidence verification
│   ├── opportunity_agent/         # Opportunity scoring
│   ├── innovation_classification_agent/ # Innovation type
│   ├── product_translation_agent/ # JTBD to PRD mapping
│   ├── concept_agent/             # HMW concept generation
│   ├── research_planning_agent/   # Next steps recommendation
│   ├── roadmap_agent/             # Product roadmap
│   ├── validation_agent/          # Validation plans
│   └── gtm_agent/                 # Go-to-market strategy
├── validators/                    # Python validation scripts
│   ├── evidence_checker.py        # Evidence source check
│   ├── jtbd_quality_checker.py    # 5T principles
│   ├── hallucination_checker.py   # AI fabrication detection
│   ├── confidence_score.py        # Weighted confidence
│   ├── context_validator.py       # Context completeness
│   ├── need_validator.py          # Need classification
│   ├── outcome_validator.py       # Outcome quality
│   ├── switch_validator.py        # Switch analysis
│   └── opportunity_validator.py   # Scoring accuracy
├── templates/                     # Output templates
│   ├── innovation_brief.md        # Executive summary
│   ├── go_nogo.md                 # Decision framework
│   ├── insight_report.md          # Full insight report
│   ├── persona_template.md        # Persona profile
│   ├── context_map.md             # Context map
│   ├── switch_analysis.md         # Switch report
│   ├── jtbd_statement.md          # Job statement
│   ├── job_map.md                 # Process map
│   ├── opportunity_matrix.md      # Opportunity ranking
│   ├── product_definition.md      # PRD mapping
│   ├── concept_card.md            # Concept card
│   ├── validation_plan.md         # Validation plan
│   ├── roadmap.md                 # Product roadmap
│   └── gtm_strategy.md            # Go-to-market plan
├── frameworks/                    # 14 JTBD methodology docs
└── examples/                      # 4 case studies
```

---

## Roadmap

- Persistent Knowledge Memory (database-backed)
- Multi-project workspace support
- Data source connectors (CSV auto-import, API integrations)
- Collaborative review workflows
- Export to Notion, Jira, Confluence
- Custom analysis mode builder
- AI-moderated user interview module
- Quantified confidence dashboard

---

<div align="center">
  <sub>Built with JTBD 2.0 methodology. An AI Customer Innovation Copilot, not just a JTBD analysis tool.</sub>
</div>

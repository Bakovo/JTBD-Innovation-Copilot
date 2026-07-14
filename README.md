
# JTBD-Innovation-Copilot

An AI-native Customer Insight and Innovation Copilot that guides product teams from research planning to evidence-backed product decisions.

---

## 为什么需要这个 Copilot

产品团队将 70% 的创新精力投入到用户不认可的事情上。根源不是缺乏数据，而是从用户数据到产品决策之间缺乏结构化思考。

这个 Copilot 基于 JTBD 方法论，通过多 Agent 工作流，将原始用户数据转化为有证据支撑的产品决策。

它不替代产品经理。它帮助产品经理思考。

---

## 适用人群

| 角色 | 它能为你做什么 |
|------|-------------|
| 产品经理 | 从用户数据到产品需求，全程可追溯证据 |
| 用户研究员 | 结构化访谈分析、模式识别、洞察提取 |
| 创新负责人 | 机会识别、概念生成、创新类型分类 |
| 产品总监 | 证据驱动的优先级排序、Go/No-Go 决策、战略路线图 |
| 创业者 | 用户需求发现、产品市场匹配验证、MVP 定义 |

---

## 使用场景

- **用户需求发现**：上传访谈记录 → 获得 JTBD 陈述 + 优先级排序的机会
- **流失分析**：分析退出访谈 → Four Forces 分析 → 留存机会排序
- **竞品分析**：通过 JTBD 透镜绘制竞争格局 → 识别非消费机会
- **概念验证**：将产品概念与用户任务对比 → 获得验证计划 + 证据缺口
- **创新探索**：发现未被满足的任务 → 分类创新类型 → 生成产品概念
- **购买行为分析**：分析决策旅程 → 切换时间线 + 触发因素 → GTM 策略

---

## 架构

```
用户数据
  ↓
Research Strategy Agent → 模式选择（Quick / Standard / Expert）
  ↓
Pipeline Dispatch → Agent 执行
  ↓
Human Checkpoints ← 用户审核
  ↓
Shared Context Memory
  ↓
Evidence Validation → Go/No-Go Decision
  ↓
Research Planning → 下一步建议
```

### Insight Pyramid（洞察金字塔）

```
原始数据 → 观察 → 模式 → 洞察 → Job → 机会 → 策略
```

所有 Agent 输出必须标记当前所属的金字塔层级。禁止从原始数据直接跳到策略。

---

## 分析模式

| 模式 | 输出 | 检查点 | 耗时 | 适用场景 |
|------|------|--------|------|---------|
| Quick | JTBD + 痛点 + 机会摘要 | 无 | 5-10 分钟 | 快速了解、初探信号 |
| Standard | 画像 + 情景 + JTBD + 需求 + 机会排序 | 2 个 | 20-30 分钟 | 一般产品研究 |
| Expert | 完整 + 竞品 + 冲突 + 路线图 + GTM + 研究计划 | 5 个 | 60-90 分钟 | 创新项目、战略决策 |

系统会根据你的输入自动推荐模式。你可以覆盖。

---

## 人机交互检查点

Copilot 会在关键阶段暂停，等待你的审核：

| 阶段 | 让你回答的问题 |
|------|-------------|
| 画像完成后 | 这个用户画像准确吗？ |
| 情景完成后 | 这些场景准确吗？ |
| JTBD 完成后 | 这些陈述符合你对用户的了解吗？ |
| 机会排序完成后 | 这些优先级符合你的判断吗？ |
| 概念生成完成后 | 这些概念值得推进吗？ |

在每个检查点你可以：确认 / 修改 / 跳过 / 重新分析。

---

## 快速开始

### 前提

- Codex 平台，Skill 自动发现已启用
- 用户研究数据（访谈、调查、评论、记录）

### 使用方法

将用户研究数据提供给 Codex，描述你需要的分析：

```
"分析这 12 份访谈记录，告诉我用户需要什么"
"这里有 500 份问卷结果，帮我找创新机会"
"用户为什么流失？我有 8 份退出访谈"
"快速看一下这些应用商店评论"
```

Copilot 会自动：
1. 检测你的目标并推荐分析模式
2. 运行相应的 Pipeline
3. 在检查点暂停等待你的审核
4. 输出有证据支撑的建议
5. 告诉你下一步应该做什么研究

### 支持的输入格式

| 格式 | 示例 |
|------|------|
| 访谈记录 | 原始文本，支持中英文 |
| CSV / Excel | 问卷结果、结构化反馈 |
| PDF | 研究报告 |
| TXT | 评论、反馈、工单 |

---

## 完整工作流

```
Step 1  Research Strategy Agent → 检测目标 + 推荐模式
Step 2  Knowledge Memory → 检查历史分析记录
Step 3  Data Quality Agent → 评估数据质量
Step 4  Observation Agent → 发现言行差距
Step 5  Persona Agent → 构建用户画像
           ← 检查点：审核画像
Step 6  Context Agent → 绘制情景地图
           ← 检查点：审核情景（Expert）
Step 7  Switch Agent / JTBD Agent → 提取任务
           ← 检查点：审核 JTBD
Step 8  Need Agent + Outcome Agent → 定义需求
Step 9  Competition Agent → 竞争分析（Expert）
Step 10 Conflict Detection Agent → 冲突检测（Expert）
Step 11 Evidence Validation → 证据验证
Step 12 Opportunity Agent → 评分排序
           ← 检查点：审核机会（Expert）
Step 13 Innovation Classification → 创新类型（Expert）
Step 14 Product Translation + Concept → 概念生成（Expert）
           ← 检查点：审核概念（Expert）
Step 15 Research Planning Agent → 下一步建议
Step 16 Decision Copilot → Go / Need More Research / No-Go
```

---

## 输出清单

| 输出 | 说明 | 可用模式 |
|------|------|---------|
| 执行摘要 | 3 分钟看懂核心发现 | 全部 |
| 用户画像 | 身份、行为、动机 | Standard, Expert |
| 情景地图 | 何时、何地、何人、前后状态 | Standard, Expert |
| 切换分析 | 时间线 + Four Forces | Standard, Expert |
| JTBD 陈述 | When + I want to + So I can | 全部 |
| Job Map | 8 步任务流程 | Standard, Expert |
| 需求分析 | 痛点 / 收益分类 | 全部 |
| 期望结果 | 可测量的结果陈述 | Standard, Expert |
| 竞争地图 | 直接 + 间接 + 非消费 | Expert |
| 冲突地图 | 用户需求矛盾 | Expert |
| 机会排序 | 评分 + 分类 | 全部 |
| 创新分类 | 创新类型 | Expert |
| 概念卡片 | HMW 产品概念 | Expert |
| 验证计划 | 验证假设的研究方案 | Expert |
| 产品路线图 | 三阶段计划 | Expert |
| GTM 策略 | 定位 + 渠道 + 发布 | Expert |
| Innovation Brief | 一页执行摘要 | Expert |
| 研究计划 | 下一步研究建议 | Expert |

---

## 局限性

- 这是一个 AI Copilot，不能替代真实用户研究。所有输出应经过真实用户验证。
- 洞察质量取决于输入数据的质量和多样性。
- JTBD 分析在定性数据（访谈、观察）上效果最好。纯定量数据（仅问卷）会产生较浅的洞察。
- Copilot 的领域知识仅限于你提供的数据。它不具备预先存在的行业知识。
- 非消费分析需要来自不使用当前解决方案的用户数据。
- 知识记忆在当前会话内持续。跨会话记忆存储在 shared_context 中，尚未具备持久化数据库。

---

## 常见问题

**问：这个 Copilot 能替代用户访谈吗？**
不能。它帮助你更系统地分析访谈数据。你仍然需要与真实用户交谈。

**问：我需要什么数据？**
至少需要用户访谈记录或包含开放性问题的问卷结果。数据越多，洞察越好。

**问：仅用问卷数据可以吗？**
可以，但置信度会较低。定性数据（访谈、观察）产生最丰富的 JTBD 洞察。

**问：它和情感分析或主题分析有什么不同？**
情感分析告诉你用户是否开心。JTBD 分析告诉你用户想要达成什么进展、以及现有方案为什么不够。

**问：支持中文吗？**
支持。中文、英文和中英混合输入均可。

**问：可以自定义工作流吗？**
可以。分析模式（Quick/Standard/Expert）让你控制深度。检查点让你在任何阶段暂停审核。

---

## 项目结构

```
customer-innovation-copilot/
├── SKILL.md                       # 执行入口
├── README.md                      # 本文件
├── execution/                     # 执行策略文档
├── context/                       # 共享上下文
├── config/                        # 配置文件（6 个）
├── agents/                        # Agent 模块（22 个）
│   ├── entry/                     # 入口层（3 个 Agent）
│   ├── analysis/                  # 分析层（4 个 Agent）
│   ├── discovery/                 # 发现层（3 个 Agent）
│   ├── definition/                # 定义层（2 个 Agent）
│   ├── strategy/                  # 策略层（3 个 Agent）
│   ├── decision/                  # 决策层（2 个 Agent）
│   └── execution/                 # 执行层（5 个 Agent）
├── validators/                    # 验证器（9 个）
│   ├── core/                      # 通用验证器
│   └── dimension/                 # 维度验证器
├── templates/                     # 输出模板（15 个）
│   ├── brief/                     # 摘要模板
│   └── reports/                   # 报告模板
├── frameworks/                    # JTBD 方法论参考（14 份）
└── examples/                      # 案例研究（4 份）
```

---

## 路线图

- 持久化知识记忆（数据库支持）
- 多项目工作空间
- 数据源连接器（CSV 自动导入、API 集成）
- 协作审核工作流
- 导出到 Notion、Jira、Confluence
- 自定义分析模式构建器
- AI 主持的用户访谈模块
- 量化置信度仪表板

---


# JTBD-Innovation-Copilot

An AI-native Customer Insight and Innovation Copilot that guides product teams from research planning to evidence-backed product decisions.

> People do not buy products. They hire products to make progress.

---

## Why This Exists

Product teams spend 70% of innovation effort on things users don't value. The root cause is not lack of data, but lack of structured thinking between user data and product decisions.

This copilot applies JTBD methodology in a structured, multi-agent workflow that transforms raw user data into evidence-backed product decisions.

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
User Data
  ↓
Research Strategy Agent → Mode Selection (Quick/Standard/Expert)
  ↓
Pipeline Dispatch → Agent Execution
  ↓
Human Checkpoints ← User Review
  ↓
Shared Context Memory
  ↓
Evidence Validation → Go/No-Go Decision
  ↓
Research Planning → Next Steps
```

### The Insight Pyramid

```
Raw Data → Observation → Pattern → Insight → Job → Opportunity → Strategy
```

Every agent output must tag its pyramid layer. No skipping from raw data to strategy.

---

## Analysis Modes

| Mode | Outputs | Checkpoints | Time | When to Use |
|------|--------|-------------|------|-------------|
| Quick | JTBD + Pains + Opportunity Summary | None | 5-10 min | First look, early signal |
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

Copy your user research data into Codex and describe what you need:

```
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
Step 1  Research Strategy Agent → Detect goal + recommend mode
Step 2  Knowledge Memory → Check for historical insights
Step 3  Data Quality Agent → Assess data fitness
Step 4  Observation Agent → Surface says-vs-does gaps
Step 5  Persona Agent → Build user profiles
           ← Checkpoint: Review Persona
Step 6  Context Agent → Map user situations
           ← Checkpoint: Review Context (Expert only)
Step 7  Switch Agent / JTBD Agent → Extract jobs
           ← Checkpoint: Review JTBD
Step 8  Need Agent + Outcome Agent → Define needs
Step 9  Competition Agent → Map alternatives (Expert)
Step 10 Conflict Detection Agent → Find tensions (Expert)
Step 11 Evidence Validation → Check all insights
Step 12 Opportunity Agent → Score + rank
           ← Checkpoint: Review Opportunities (Expert)
Step 13 Innovation Classification → Type innovation (Expert)
Step 14 Product Translation + Concept → Generate concepts (Expert)
           ← Checkpoint: Review Concepts (Expert)
Step 15 Research Planning Agent → Recommend next steps
Step 16 Decision Copilot → Go / Need More Research / No-Go
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
├── execution/                     # Execution strategy docs
├── context/                       # Shared context
├── config/                        # 6 config files
├── agents/                        # 22 agent modules
│   ├── entry/                     # 3 entry agents
│   ├── analysis/                  # 4 analysis agents
│   ├── discovery/                 # 3 discovery agents
│   ├── definition/                # 2 definition agents
│   ├── strategy/                  # 3 strategy agents
│   ├── decision/                  # 2 decision agents
│   └── execution/                 # 5 execution agents
├── validators/                    # 9 validators
│   ├── core/                      # General validators
│   └── dimension/                 # Dimension validators
├── templates/                     # 15 output templates
│   ├── brief/                     # Summary templates
│   └── reports/                   # Report templates
├── frameworks/                    # 14 JTBD references
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
  <sub>Built with JTBD methodology. An JTBD-Innovation-Copilot, not just a JTBD analysis tool.</sub>
</div>

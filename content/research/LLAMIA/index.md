---
title: "Internalizing Heterogeneous Agents in Language Model Reasoning"
authors:
- S I Harini
- Somesh Singh
- Yaman Kumar Singla
- Rajiv Ratn Shah
- David Doermann
- Balaji Krishnamurthy

date: "2026-08-01T00:00:00Z"
doi: ""

publishDate: "2026-08-01T00:00:00Z"

publication_types: ["conference"]

publication: "Conference on Empirical Methods in Natural Language Processing (EMNLP)"
publication_short: "EMNLP"

abstract: "LLMs are increasingly deployed as orchestrators that coordinate specialized subagents to solve complex tasks through natural language. However, in many important domains like game playing and robotics the strongest available agents are not language models. Integrating non-language agents with LLMs would require verbalization — compressing their rich continuous representations into sparse textual summaries at each interaction step. In this work we introduce the concept of latent state internalization: instead of verbalizing the non-language agent's state, we project its internal continuous representations directly into the LLM's chain of thought as learned state tokens. We show that training LLMs and subagents through internalization and reinforcement learning can solve previously unsolvable tasks, and a single model can outperform existing state-of-the-art task-specific methods trained over 100x more data. To evaluate these collaborative abilities, we introduce LLAMIA-Bench, a suite of six collaborative chess tasks from prominent AI literature spanning behavior cloning, state understanding, and natural-language explanation of actions and policies. These tasks cannot be solved by LLMs or subagents independently, making them a perfect testbed for studying collaboration. Our experiments reveal a consistent verbalization debt: verbalizing the subagent's state consistently trails internalizing it, and this gap does not shrink as the LLM scales from 4B to 14B parameters. A single 14B model, LLAMIA (Large Language and Action Models with Internal Agents), trained under this paradigm matches or exceeds both dedicated task specialists and the strongest verbalization-based pipeline, GPT-5.1 with tool access, across all benchmark tasks, and generalizes out-of-distribution where these specialists collapse."

summary: ""

tags:
- Large Language Models
- Multi-Agent Systems
- Reinforcement Learning
- Chain of Thought
- Behavioral Sciences

featured: true

links:
url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: "https://behavior-in-the-wild.github.io/llamia"
url_slides: ""
url_source: ""
url_video: ""

image:
  caption: "LLAMIA: Internalizing Heterogeneous Agents in Language Model Reasoning"
  focal_point: "Center"
  preview_only: false
  alt_text: "LLAMIA architecture: latent state internalization interleaves language, action, and subagent latent state tokens in the LLM's chain of thought"

projects: []
slides: ""
---

---
title: "Budget-Aware Evidence Selection for Post-Hoc LLM Attribution"
authors:
- Vishak Prasad C
- Ashutosh Mulchandani
- Pulkit
- Sumit Bhatia
- Ganesh Ramakrishnan

date: "2026-11-26T00:00:00Z"
doi: ""

publishDate: "2026-11-26T00:00:00Z"

publication_types: ["conference"]

publication: "NeurIPS Workshop on Data Attribution and Provenance (ATTRIB)"
publication_short: "NeurIPS Workshop"

abstract: "Post-hoc attribution for Large Language Models (LLMs) aims to support, or justify, LLM’s generated response by providing a concise set of passages that are retrieved from an external corpus that support (i.e., logically entail) the output. Natural Language Inference (NLI) has become a central mechanism for post-hoc attribution of LLM outputs, allowing retrieved passages to be assessed according to whether they entail a generated answer. However, existing NLI-based approaches typically score passages independently and select the highest-scoring candidates. This becomes problematic when attribution operates under a strict citation budget: several highly entailing passages may provide redundant evidence, while complementary passages that collectively offer stronger support may be excluded. We therefore study budget-constrained attribution as a selection problem built on top of NLI-based attribution. We introduce RESPATT (Response Attribution), which selects a subset of k passages from an initially retrieved pool using a submodular objective that combines NLI-based answer entailment, retrieval relevance, and redundancy reduction. This formulation preserves NLI as the primary attribution signal while explicitly reasoning about the utility of the selected evidence set under a fixed budget. Experiments on question-answering datasets with two open-source LLMs show that RESPATT consistently outperforms standard baselines, yielding stronger post-hoc attribution in budget-constrained settings. We make our code and examples available at the project’s repository."

summary: ""

tags:
- LLM Attribution
- Natural Language Inference
- Submodular Optimization
- Retrieval-Augmented Generation

featured: false

links:
url_pdf: "https://neurips.cc/virtual/2026/loc/sydney/161675"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""


projects: []
slides: ""
---

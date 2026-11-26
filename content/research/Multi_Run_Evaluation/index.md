---
title: "Agentic Systems Need Multi-Run Evaluation: A Study of Retrieval and Response Variability in a Deployed Enterprise RAG System"
authors:
- Karan Gupta
- Sumit Bhatia
- Yunyao Li

date: "2026-10-21T00:00:00Z"
doi: ""

publishDate: "2026-10-21T00:00:00Z"

publication_types: ["conference"]

publication: "NeurIPS Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks (AABA4ET)"
publication_short: "NeurIPS Workshop"

abstract: "Previous RAG systems have mostly been evaluated in a single-run setting, and with the advent of agentic RAG, systems are still often evaluated the same way. However, agentic RAG systems introduce a source of run-to-run variability, since several of their components make decisions non-deterministically. Such systems typically comprise a retrieval stage followed by a generation stage, and the retrieval stage in particular can behave differently across runs. For example, the agent might issue a different number of parallel searches from one run to the next, which alters the retrieved documents and therefore the final answer. In this paper we study this behavior in a deployed agentic RAG system for product-documentation questions, running each of 739 questions ten times and analyzing the execution traces to find where different runs first diverge. We find a substantial gap between success in any run and success in every run: the retrieval hit rate is 69.4% when the correct page is found in at least one run, but 50.9% when it must be found in all ten. Responses also stay similar in meaning while varying in wording, with an average BERTScore of 0.90 and a BLEU of 0.49. Trace-level analysis shows that retrieval is the largest source of divergence (43.9%), and the number of parallel searches at the first retrieval step alone accounts for 20.1% of divergent pairs. Taken together, these results show that single-run evaluation can hide reliability and consistency issues in agentic RAG systems, and that multi-run evaluation is necessary to reveal them."

summary: ""

tags:
- Agentic RAG
- Evaluation
- Reliability
- Enterprise AI Assistant

featured: false

links:
url_pdf: "https://arxiv.org/abs/2611.31266"
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

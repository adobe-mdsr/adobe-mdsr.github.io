---
title: "On the Effect of Instruction Tuning Loss on Generalization"
authors:
- Anwoy Chatterjee
- H S V N S Kowndinya Renduchintala
- Sumit Bhatia
- Tanmoy Chakraborty

date: "2025-07-28T00:00:00Z"
doi: "10.48550/arXiv.2507.07817"

publishDate: "2025-07-28T00:00:00Z"

publication_types: ["journal preprint"]

publication: "Transactions of the Association for Computational Linguistics"
publication_short: "TACL"

abstract: "Instruction Tuning has emerged as a pivotal post-training paradigm that enables pre-trained language models to better follow user instructions. Despite its significance, little attention has been given to optimizing the loss function used. A fundamental, yet often overlooked, question is whether the conventional auto-regressive objective - where loss is computed only on response tokens, excluding prompt tokens - is truly optimal for instruction tuning. In this work, we systematically investigate the impact of differentially weighting prompt and response tokens in instruction tuning loss, and propose Weighted Instruction Tuning (WIT) as a better alternative to conventional instruction tuning. Through extensive experiments on five language models of different families and scale, three finetuning datasets of different sizes, and five diverse evaluation benchmarks, we show that the standard instruction tuning loss often yields suboptimal performance and limited robustness to input prompt variations. We find that a low-to-moderate weight for prompt tokens coupled with a moderate-to-high weight for response tokens yields the best-performing models across settings and also serve as better starting points for the subsequent preference alignment training. These findings highlight the need to reconsider instruction tuning loss and offer actionable insights for developing more robust and generalizable models. Our code is open-sourced at https://github.com/kowndinya-renduchintala/WIT."
summary: ""

tags:
- Natural Language Processing
- Language Models
- Instruction Tuning
- Instruction Tuning Loss
- LLM Post Training

featured: false


links:
url_pdf: "https://arxiv.org/abs/2507.07817"
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
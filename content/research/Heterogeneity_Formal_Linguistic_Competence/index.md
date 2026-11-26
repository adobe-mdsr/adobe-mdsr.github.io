---
title: "Heterogeneity in Formal Linguistic Competence of Language Models: Is Data the Real Bottleneck?"
authors:
- H S V N S Kowndinya Renduchintala
- Sumit Bhatia

date: "2026-07-01T00:00:00Z"
doi: ""

publishDate: "2026-07-01T00:00:00Z"

publication_types: ["conference"]

publication: "Findings of the Association for Computational Linguistics (ACL)"
publication_short: "ACL (Findings)"

abstract: "Large Language Models (LLMs) exhibit a puzzling disparity in their formal linguistic competence: while they learn some linguistic phenomena with near-perfect mastery, they often perform below chance on others, even after training on trillions of tokens. In this work, we investigate whether these failures stem from inherent architectural limitations or simply the scarcity of these specific grammatical constructions in web-scale corpora. We pre-train simple GPT-2 Small (124M) models on a 100M-token random sample of the FineWeb corpus and intervene by injecting a minimal amount (1%) of synthetic data targeting specific linguistic phenomena. We find that this targeted intervention substantially improves model performance in 8 out of the 9 worst-performing BLiMP paradigms – notably the accuracy on a specific paradigm, only_npi_scope, surges from 20.9% to 69.4%. Furthermore, we observe that these interventions generally preserve or slightly improve aggregate performance. However, while we also identify a resistant phenomenon, principle_A_c_command, whose performance remains below chance even after our data augmentation, our findings do serve as an optimistic existence proof that even small language models can substantially improve on those linguistic phenomena on which models typically perform poorly, provided the pre-training data contains sufficient exposure to them. This suggests that efforts towards human-scale language modeling may benefit greatly by focusing on data composition. The code to reproduce our results is open-sourced at https://github.com/kowndinyarenduchintala/heterogeneity-in-formallinguistic-competence"

summary: ""

tags:
- Language Models
- Pre-training Data
- Linguistic Competence
- BLiMP
- Synthetic Data

featured: false

links:
url_pdf: "https://aclanthology.org/2026.findings-acl.224.pdf"
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

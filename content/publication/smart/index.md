---
title: "SMART: Submodular Data Mixture Strategy for Instruction Tuning"
authors:
- H S V N S Kowndinya Renduchintala
- Sumit Bhatia
- Ganesh Ramakrishnan

date: "2024-08-11T00:00:00Z"
doi: "10.18653/v1/2024.findings-acl.766"

publishDate: "2024-08-11T00:00:00Z"

publication_types: ["conference"]

publication: "Findings of the Association for Computational Linguistics: ACL"
publication_short: "ACL 2024 (Findings)"

abstract: "Instruction Tuning involves finetuning a language model on a collection of instruction-formatted datasets in order to enhance the generalizability of the model to unseen tasks. Studies have shown the importance of balancing different task proportions during finetuning, but finding the right balance remains challenging. Unfortunately, there’s currently no systematic method beyond manual tuning or relying on practitioners’ intuition. In this paper, we introduce SMART (Submodular data Mixture strAtegy for instRuction Tuning) — a novel data mixture strategy which makes use of a submodular function to assign importance scores to tasks which are then used to determine the mixture weights. Given a fine-tuning budget, SMART redistributes the budget among tasks and selects non-redundant samples from each task. Experimental results demonstrate that SMART significantly outperforms traditional methods such as examples proportional mixing and equal mixing. Furthermore, SMART facilitates the creation of data mixtures based on a few representative subsets of tasks alone and through task pruning analysis, we reveal that in a limited budget setting, allocating budget among a subset of representative tasks yields superior performance compared to distributing the budget among all tasks. The code for reproducing our results is open-sourced at https://github.com/kowndinya-renduchintala/SMART."
summary: ""

tags:
- Natural Language Processing
- Language Models
- Instruction Tuning
- Data Efficiency
- Submodularity
- Data Mixtures

featured: false


links:
url_pdf: "https://aclanthology.org/2024.findings-acl.766.pdf"
url_code: ""
url_dataset: ""
url_poster: "https://kowndinya-renduchintala.github.io/assets/pdf/2024.findings-acl.766.poster.pdf"
url_project: ""
url_slides: ""
url_source: ""
url_video: "https://youtu.be/o4GMJRWl0nU"

  alt_text: "Generated scanpaths over text samples taken from various natural language processing (NLP) tasks."

projects: []
slides: ""
---
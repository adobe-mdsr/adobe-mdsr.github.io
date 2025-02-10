---
title: "POSIX: Prompt Sensitivity Index for Large Language Models"
authors:
- Anwoy Chatterjee
- H S V N S Kowndinya Renduchintala
- Sumit Bhatia
- Tanmoy Chakraborty

date: "2024-11-12T00:00:00Z"
doi: "10.18653/v1/2024.findings-emnlp.852"

publishDate: "2024-11-11T00:00:00Z"

publication_types: ["conference"]

publication: "Findings of the Association for Computational Linguistics: EMNLP 2024"
publication_short: "EMNLP 2024 (Findings)"

abstract: "Despite their remarkable capabilities, Large Language Models (LLMs) are found to be surprisingly sensitive to minor variations in prompts, often generating significantly divergent outputs in response to minor variations in the prompts, such as spelling errors, alteration of wording or the prompt template. However, while assessing the quality of an LLM, the focus often tends to be solely on its performance on downstream tasks, while very little to no attention is paid to prompt sensitivity. To fill this gap, we propose POSIX – a novel PrOmpt Sensitivity IndeX as a reliable measure of prompt sensitivity, thereby offering a more comprehensive evaluation of LLM performance. The key idea behind POSIX is to capture the relative change in loglikelihood of a given response upon replacing the corresponding prompt with a different intent-preserving prompt. We provide thorough empirical evidence demonstrating the efficacy of POSIX in capturing prompt sensitivity and subsequently use it to measure and thereby compare prompt sensitivity of various open source LLMs. We find that merely increasing the parameter count or instruction tuning does not necessarily reduce prompt sensitivity whereas adding some few-shot exemplars, even just one, almost always leads to significant decrease in prompt sensitivity. We also find that alterations to prompt template lead to the highest sensitivity in the case of MCQ type tasks, whereas paraphrasing results in the highest sensitivity in open-ended generation tasks. The code for reproducing our results is open-sourced at https://github.com/kowndinya-renduchintala/POSIX."
summary: ""

tags:
- Natural Language Processing
- Language Models
- Prompt Sensitivity

featured: false


links:
url_pdf: "https://aclanthology.org/2024.findings-emnlp.852.pdf"
url_code: ""
url_dataset: ""
url_poster: "https://kowndinya-renduchintala.github.io/assets/pdf/2024.findings-emnlp.852.poster.pdf"
url_project: ""
url_slides: ""
url_source: ""
url_video: "https://youtu.be/WV1hfWmIAIM"

projects: []
slides: ""
---
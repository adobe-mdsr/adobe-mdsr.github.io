---
title: "Learning What Comes Next, Beyond Similarity: Directional Causal Dependencies in Text for Enterprise Applications"
authors:
- Atul Singh
- Milan Aggarwal
- Nikaash Puri
- Sumit Bhatia
- Jitendra Ajmera

date: "2026-11-26T00:00:00Z"
doi: ""

publishDate: "2026-11-26T00:00:00Z"

publication_types: ["conference"]

publication: "AAAI Conference on Innovative Applications of Artificial Intelligence (IAAI)"
publication_short: "IAAI"

abstract: "Dense text embeddings are foundational to semantic search, RAG, and enterprise conversational assistants that serve users not only for information discovery but for executing complex multi-step workflows. However, these embeddings are not trained to capture sequential dependencies which are critical for applications such as ordering steps for workflow execution and suggesting what a user should ask or read next for better engagement. Generative LLMs cannot fill this gap at scale: these applications require knowledge of full enterprise documentation, feeding it as context causes prohibitive context bloat, and re-deriving dependencies for every sample compounds the cost further. Relation extraction methods trained on narrative text suffer from domain shift when applied to enterprise documents. To address this, we provide a generic data construction approach that mines directional text pairs from enterprise documentation at within-document and cross-document levels (dataset to be released), and formalize the core problem as Causal Embeddings: learning an asymmetric scoring function sθ(A, B) ≈ P(A precedes B) between text pairs. To learn such representations effectively, we introduce Reasoning-CE: a cross-encoder that processes text pairs such that its representations are aligned with natural language rationales explaining the directional dependency between texts via a training-only auxiliary decoder, substantially outperforming label-only training at no added inference cost. Reasoning-CE achieves 86.1% pairwise accuracy and 89.5% exact workflow-ordering accuracy at 434M parameters, outperforming ICL and LoRA fine-tuned models up to 14B parameters and a frontier API model. Further, applied to a deployed follow-up question system, causal reranking raises LLM-judged follow-up suggestion quality by 12 points."

summary: ""

tags:
- Text Embeddings
- Causal Dependencies
- Enterprise AI Assistant
- Follow-up Suggestions

featured: false

links:
url_pdf: ""
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

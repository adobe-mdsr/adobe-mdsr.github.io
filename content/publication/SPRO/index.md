---
title: "SPRO: Improving Image Generation via Self-Play"
authors:
- Ritika Jha
- Aanisha Bhattacharyya
- Yaman Kumar Singla
- Rajiv Ratn Shah
- Changyou Chen
- Balaji Krishnamurthy

date: "2025-10-01T00:00:00Z"
doi: ""

publishDate: "2025-10-01T00:00:00Z"

publication_types: ["conference"]

publication: "Conference on Neural Information Processing Systems"
publication_short: "NeurIPS"

abstract: "Recent advances in diffusion models have dramatically improved image fidelity and diversity. However, aligning these models with nuanced human preferences - such as aesthetics, engagement, and subjective appeal - remains a key challenge due to the scarcity of large-scale human annotations. Collecting such data is both expensive and limited in diversity. To address this, we leverage the reasoning capabilities of vision-language models (VLMs) and propose Self-Play Reward Optimization (SPRO), a scalable, annotation-free training framework based on multimodal self-play. SPRO learns to jointly align prompt and image generation with human preferences by iteratively generating, evaluating, and learning to refine outputs using synthetic reward signals such as aesthetics and human engagement. This self-improving feedback loop eliminates the need for external supervision. SPRO comprises three stages: (1) SPRO-Prompt, which trains a Guider-VLM via self-play to generate diverse, high-reward prompts targeting objectives such as PickScore (user preference), LAION-Aesthetics, and EngageNet (engagement); (2) SPRO-Image, which fine-tunes the diffusion model on high-reward images derived from these prompts; and (3) SPRO-Multimodal (SPRO-MM), which integrates both components for full end-to-end alignment. Without relying on human-labeled data, SPRO achieves an average 30% improvement across preference objectives. Moreover, its generated prompts generalize across both open- and closed-source diffusion models. Through iterative self-play, SPRO discovers prompting strategies rarely authored by humans such as emphasizing visual harmony for aesthetics or leveraging shadow-based cues for engagement. SPRO offers a scalable path toward aligning generative models with complex subjective human values."

summary: ""

tags:
- Computer Vision
- Diffusion Models
- Self-Play
- Image Generation
- Vision-Language Models
- Behavior in the Wild

featured: true


links:
url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: "https://neurips.cc/virtual/2025/poster/119483"
url_slides: ""
url_source: ""
url_video: ""

image:
  caption: "SPRO: Self-Play Reward Optimization for image generation"
  focal_point: "SPRO"
  preview_only: false
  alt_text: "SPRO: Self-Play Reward Optimization for image generation"

projects: []
slides: ""
---


---
title: "ZIPP: Zero-shot Image Personalization from Personas"
authors:
- S I Harini
- Somesh Singh
- Yaman Kumar Singla
- David Doermann
- Rajiv Ratn Shah

date: "2026-06-01T00:00:00Z"
doi: ""

publishDate: "2026-06-01T00:00:00Z"

publication_types: ["conference"]

publication: "European Conference on Computer Vision (ECCV)"
publication_short: "ECCV"

abstract: "Text-to-image diffusion models are increasingly deployed in creative contexts, yet remain impersonal — optimized for aggregate aesthetics rather than individual taste. Human preferences are also pluralistic: the same person may want muted, nostalgic portraits but vibrant, saturated street photography. Existing methods need dense interaction histories or per-user fine-tuning, fail in cold-start settings, and collapse each user's context-dependent preferences into one static style. We introduce zero-shot image personalization from personas (ZIPP), which conditions generation on natural-language personas — concise descriptors of a user's identity, interests, and aesthetic sensibilities — with no user-specific data and no weight updates. An LLM roleplays the persona to rewrite prompts, steering a frozen diffusion model toward taste-aligned outputs. Persona mining at scale is achieved via an inductive Graph Attention Network over a 23M-user Reddit interaction graph, trained with dual contrastive objectives that align graph structure with users' visual behavior. We also introduce ZIPBench, the first zero-shot image-personalization benchmark, pairing 1.5K users with graph-mined personas and 40K generated images. Across four benchmarks and 14 LLMs from five families, persona conditioning improves personalization by 13–20%, with frontier models gaining most; few-shot ZIPP matches or exceeds fine-tuned baselines trained on 100+ examples per user. ZIPP best preserves intra-user preference diversity (lowest CMMD, 0.16 vs. 0.55), and human raters prefer ZIPP 79% of the time over generic generation and every fine-tuned baseline."

summary: ""

tags:
- Image Personalization
- Diffusion Models
- Vision-Language Models
- Personas
- Zero-shot
- Graph Neural Networks
- Behavioral Sciences

featured: true

links:
url_pdf: "https://arxiv.org/pdf/2606.08841"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: "https://behavior-in-the-wild.github.io/zipp"
url_slides: ""
url_source: ""
url_video: ""

image:
  caption: "ZIPP: Zero-shot Image Personalization from Personas"
  focal_point: "Center"
  preview_only: false
  alt_text: "ZIPP overview: persona discovery, verbalization, and persona-conditioned prompt rewriting"

projects: []
slides: ""
---

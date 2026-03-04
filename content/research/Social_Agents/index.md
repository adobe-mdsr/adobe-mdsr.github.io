---
title: "Social Agents: Collective Intelligence Improves LLM Predictions"
authors:

- Aanisha Bhattacharyya
- Abhilekh Borah
- Yaman Kumar Singla
- Rajiv Ratn Shah
- Changyou Chen
- Balaji Krishnamurthy

date: "2026-01-26T00:00:00Z"
doi: ""

publishDate: "2026-01-26T00:00:00Z"

publication_types: ["conference"]

publication: "International Conference on Learning Representations"
publication_short: "ICLR"

abstract: "In human society, collective decision making has often outperformed the judgment of individuals. Classic examples range from estimating livestock weights to predicting elections and financial markets, where averaging many independent guesses often yields results more accurate than experts. These successes arise because groups bring together diverse perspectives, independent voices, and distributed knowledge, combining them in ways that cancel individual biases. This principle, known as the Wisdom of Crowds, underpins practices in forecasting, marketing, and preference modeling. Large Language Models (LLMs), however, typically produce a single definitive answer. While effective in many settings, this uniformity overlooks the diversity of human judgments shaping responses to ads, videos, and webpages. Inspired by how societies benefit from diverse opinions, we ask whether LLM predictions can be improved by simulating not one answer but many. We introduce Social Agents, a multi-agent framework that instantiates a synthetic society of human-like personas with diverse demographic (e.g., age, gender) and psychographic (e.g., values, interests) attributes. Each persona independently appraises a stimulus such as an advertisement, video, or webpage, offering both a quantitative score (e.g., click-through likelihood, recall score, likability) and a qualitative rationale. Aggregating these opinions produces a distribution of preferences that more closely mirrors real human crowds. Across eleven behavioral prediction tasks, Social Agents outperforms single-LLM baselines by up to 67.45% on simple judgments (e.g. webpage likability) and 9.88% on complex interpretive reasoning (e.g. video memorability). Social Agents’ individual persona predictions also align with human judgments, reaching Pearson correlations up to 0.71. These results position computational crowd simulation as a scalable, interpretable tool for improving behavioral prediction and supporting societal decision making."

summary: ""

tags:
- Large Language Models
- Behavior Simulation
- Multi-agent Systems
- Social Simulation
- Behavior Understanding
- Behavior in the Wild
- Computational Marketing
- Computational Behavior Science

featured: true



links:
url_pdf: "https://openreview.net/pdf?id=73J3hsato3"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""

image:
  caption: "Social Agents: Collective Intelligence Improves LLM Predictions"
  focal_point: "Smart"
  preview_only: false
  alt_text: "Overview of the Social Agents workflow for Ad Click-Through Rate (CTR) Prediction. Given an advertisement (top-left), our framework computes its embeddings and retrieves the top-K semantically similar ads from a repository of ad embeddings. These serve as few-shot examples that aid CTR prediction. A Persona Agent Factory (bottom-left) contains personas defined by demographic attributes (e.g., age, gender) and traits (e.g., interests, occupation), following templates in Appendix Table 2. From this pool, the moderator selects a diverse panel of N personas and instantiates separate LLM agents for each. Each persona agent outputs a CTR percentile (0-100) with a brief rationale. The right-hand side shows the moderator aggregating these predictions via mean to produce a single CTR percentile, with a collective rationale that is compared against the ground-truth CTR percentile."

projects: []
slides: ""
---
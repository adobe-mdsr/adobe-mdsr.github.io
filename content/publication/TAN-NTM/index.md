---
title: "TAN-NTM: Topic Attention Networks for Neural Topic Modeling"
authors:
- Madhur Panwar
- Shashank Shailabh
- Milan Aggarwal
- Balaji Krishnamurthy

date: "2023-01-01T00:00:00Z"
doi: ""

publishDate: "2023-01-01T00:00:00Z"

publication_types: ["conference"]

publication: "ACL-IJCNLP 2021"
publication_short: "ACL-IJCNLP"

abstract: "Topic models have been widely used to learn text representations and gain insight into document corpora. To perform topic discovery, most existing neural models either take document bag-of-words (BoW) or sequence of tokens as input followed by variational inference and BoW reconstruction to learn topic-word distribution. However, leveraging topic-word distribution for learning better features during document encoding has not been explored much. To this end, we develop a framework TAN-NTM, which processes document as a sequence of tokens through a LSTM whose contextual outputs are attended in a topic-aware manner. We propose a novel attention mechanism which factors in topic-word distribution to enable the model to attend on relevant words that convey topic related cues. The output of topic attention module is then used to carry out variational inference. We perform extensive ablations and experiments resulting in ~9-15 percentage improvement over score of existing SOTA topic models in NPMI coherence on several benchmark datasets - 20Newsgroups, Yelp Review Polarity and AGNews. Further, we show that our method learns better latent document-topic features compared to existing topic models through improvement on two downstream tasks: document classification and topic guided keyphrase generation."

summary: ""

tags:
- Source Themes
featured: false

links:
url_pdf: "https://arxiv.org/abs/2012.01524"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""

image:
  caption: "Image caption"
  focal_point: ""
  preview_only: false

projects: []
slides: ""
---

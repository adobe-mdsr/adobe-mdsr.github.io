---
title: "Automatic Essay Scoring Systems are Both Overstable and Oversensitive: Explaining Why and Proposing Defenses"
authors:
- Yaman Kumar Singh
- Swapnil Parekh
- Somesh Singh
- Junyi Jessy Li
- Rajiv Ratn Shah
- Changyou Chen

date: "2023-01-01T00:00:00Z"
doi: ""

publishDate: "2023-01-01T00:00:00Z"

publication_types: ["journal"]

publication: "Dialogue & Discourse"
publication_short: "Journal"

abstract: "Deep-learning based Automatic Essay Scoring (AES) systems are being actively used in various high-stake applications in education and testing. However, little research has been put to understand and interpret the black-box nature of deep-learning-based scoring algorithms. While previous studies indicate that scoring models can be easily fooled, in this paper, we explore the reason behind their surprising adversarial brittleness. We utilize recent advances in interpretability to find the extent to which features such as coherence, content, vocabulary, and relevance are important for automated scoring mechanisms. We use this to investigate the oversensitivity (i.e., large change in output score with a little change in input essay content) and overstability (i.e., little change in output scores with large changes in input essay content) of AES. Our results indicate that autoscoring models, despite getting trained as “end-to-end” models with rich contextual embeddings such as BERT, behave like bag-of-words models. A few words determine the essay score without the requirement of any context making the model largely overstable. This is in stark contrast to recent probing studies on pre-trained representation learning models, which show that rich linguistic features such as parts-of-speech and morphology are encoded by them. Further, we also find that the models have learnt dataset biases, making them oversensitive. The presence of a few words with high co-occurrence with a certain score class makes the model associate the essay sample with that score. This causes score changes in ∼95% of samples with an addition of only a few words. To deal with these issues, we propose detection-based protection models that can detect oversensitivity and samples causing overstability with high accuracies. We find that our proposed models are able to detect unusual attribution patterns and flag adversarial samples successfully."

summary: "Deep-learning based Automatic Essay Scoring (AES) systems are being actively used in various high-stake applications in education and testing. However, little research has been put to understand and interpret the black-box nature of deep-learning-based scoring algorithms. While previous studies indicate that scoring models can be easily fooled, in this paper, we explore the reason behind their surprising adversarial brittleness. We utilize recent advances in interpretability to find the extent to which features such as coherence, content, vocabulary, and relevance are important for automated scoring mechanisms. We use this to investigate the oversensitivity (i.e., large change in output score with a little change in input essay content) and overstability (i.e., little change in output scores with large changes in input essay content) of AES. Our results indicate that autoscoring models, despite getting trained as “end-to-end” models with rich contextual embeddings such as BERT, behave like bag-of-words models. A few words determine the essay score without the requirement of any context making the model largely overstable. This is in stark contrast to recent probing studies on pre-trained representation learning models, which show that rich linguistic features such as parts-of-speech and morphology are encoded by them. Further, we also find that the models have learnt dataset biases, making them oversensitive. The presence of a few words with high co-occurrence with a certain score class makes the model associate the essay sample with that score. This causes score changes in ∼95% of samples with an addition of only a few words. To deal with these issues, we propose detection-based protection models that can detect oversensitivity and samples causing overstability with high accuracies. We find that our proposed models are able to detect unusual attribution patterns and flag adversarial samples successfully."

tags:
- AES
- Interpretability
- Adversarial Robustness

featured: true



links:
url_pdf: "https://journals.uic.edu/ojs/index.php/dad/article/view/12448"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""

image:
  caption: "Automatic Essay Scoring Systems are Both Overstable and Oversensitive: Explaining Why and Proposing Defenses"
  focal_point: "Smart"
  preview_only: false
  alt_text: "Automatic Essay Scoring Systems are Both Overstable and Oversensitive: Explaining Why and Proposing Defenses"

projects: []
slides: ""
---
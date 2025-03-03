---
title: "What Ails One-Shot Image Segmentation: A Data Perspective"
authors:
- Mayur Hemani
- Abhinav Patel
- Tejas Shimpi
- Anirudha Ramesh
- Balaji Krishnamurthy

date: "2021-01-01T00:00:00Z"
doi: ""

publishDate: "2021-01-01T00:00:00Z"

publication_types: ["conference"]

publication: "NeurIPS"
publication_short: "NeurIPS"

abstract: "One-shot image segmentation (OSS) methods enable semantic labeling of image
pixels without supervised training using an extensive dataset. They require just
one example (image, mask) pair per target class. Most neural-network based OSS
methods train on a large subset of dataset classes, and are evaluated on a disjoint
subset of classes. We posit that the data used for training induces negative biases
and affects the accuracy of these methods. Specifically, we present evidence for a
Class Negative Bias (CNB) arising from treating non-target objects as background
during training, and Salience Bias (SB), affecting the segmentation accuracy for
non-salient target class pixels. We demonstrate that by eliminating CNB and
SB, significant gains can be made over existing state-of-the-art. Next, we argue
that there is a significant disparity between real-world expectations from an OSS
method and its accuracy reported on existing benchmarks. To this end, we propose
a new evaluation dataset - Tiered One-shot Segmentation (TOSS) - based on
the PASCAL 5i and FSS-1000 datasets, and associated metrics for each tier. The
dataset enforces consistent accuracy measurement for existing methods, and affords
fine-grained insights into the applicability of a method to real applications. The
paper includes extensive experiments with the TOSS dataset on several existing
OSS methods. The intended impact of this work is to point to biases in training
and introduce nuances and uniformity in reporting results for the OSS problem.
The evaluation splits of the TOSS dataset and instructions for use are available at
https://github.com/fewshotseg/toss."

summary: ""

tags:
- One-shot
- Image Segmentation
- Semantic Labeling
- Enable
featured: false

links:
url_pdf: "https://openreview.net/pdf?id=BlcUQYxknbX"
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

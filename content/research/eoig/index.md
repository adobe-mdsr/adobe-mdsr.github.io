---
title: "Measuring And Improving Engagement of Text-to-Image Generation Models"
authors:
- Varun Khurana
- Yaman Kumar Singla
- Jayakumar Subramanian
- Changyou Chen
- Rajiv Ratn Shah
- Zhiqiang Xu
- Balaji Krishnamurthy

date: "2025-01-22T00:00:00Z"
doi: 

publishDate: "2025-01-22T00:00:00Z"

publication_types: ["conference"]

publication: "International Conference on Learning Representations (ICLR)"
publication_short: "ICLR"

abstract: "Recent advances in text-to-image generation have achieved impressive aesthetic quality, making these models usable for both personal and commercial purposes. However, in the fields of marketing and advertising, images are often created to be more engaging, as reflected in user behaviors such as increasing clicks, likes, and purchases, in addition to being aesthetically pleasing. Further, we find that existing image generation metrics like aesthetics, CLIPScore, PickScore, ImageReward, etc. fail to capture viewer engagement. To this end, we introduce the challenge of optimizing the image generation process for improved viewer engagement. In order to study image engagement and utility in real-world marketing scenarios, we collect EngagingImageNet, the first large-scale dataset of images, along with associated user engagement metrics. To address the lack of reliable metrics for assessing image utility, we use the EngagingImageNet dataset to train EngageNet, an engagement-aware Vision Language Model (VLM) that predicts viewer engagement of images by leveraging contextual information about the tweet content, enterprise details, and posting time. We then explore methods to enhance the engagement of text-to-image models, making initial strides in this direction. These include conditioning image generation on improved prompts, supervised fine-tuning of stable diffusion on high-performing images, and reinforcement learning to align stable diffusion with EngageNet-based reward signals, all of which lead to the generation of images with higher viewer engagement. Finally, we propose the Engagement Arena, to benchmark text-to-image models based on their ability to generate engaging images, using EngageNet as the evaluator, thereby encouraging the research community to measure further advances in the engagement of text-to-image modeling. These contributions provide a new pathway for advancing utility-driven image generation, with significant implications for the commercial application of image generation."
summary: ""

tags:
- Text-to-image generation
- Engagement 
- LLM-as-a-judge
- Vision-Language Models
- User Engagement
- Image Engagement
- Stable Diffusion
- Dall-E
- Behavior-in-the-Wild

featured: true


links:
url_pdf: "https://openreview.net/forum?id=TmCcNuo03f"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""

image:
  caption: "Comparison of generated images - EOIG-SD and Base stable diffusion."
  focal_point: "Smart"
  preview_only: false
  alt_text: "Comparison of generated images - EOIG-SD and Base stable diffusion."

projects: []
slides: ""
---
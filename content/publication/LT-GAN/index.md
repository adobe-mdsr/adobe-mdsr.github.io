---
title: "LT-GAN: Self-Supervised GAN with Latent Transformation Detection"
authors:
- Parth Patel
- Nupur Kumari
- Mayank Singh
- Balaji Krishnamurthy

date: "2021-01-01T00:00:00Z"
doi: ""

publishDate: "2021-01-01T00:00:00Z"

publication_types: ["conference"]

publication: "WACV , Oral"
publication_short: "WACV"

abstract: "Generative Adversarial Networks (GANs) coupled with self-supervised tasks have shown promising results in unconditional and semi-supervised image generation. We propose a self-supervised approach (LT-GAN) to improve the generation quality and diversity of images by estimating the GAN-induced transformation (i.e. transformation induced in the generated images by perturbing the latent space of generator). Specifically, given two pairs of images where each pair comprises of a generated image and its transformed version, the self-supervision task aims to identify whether the latent transformation applied in the given pair is same to that of the other pair. Hence, this auxiliary loss encourages the generator to produce images that are distinguishable by the auxiliary network, which in turn promotes the synthesis of semantically consistent images with respect to latent transformations. We show the efficacy of this pretext task by improving the image generation quality in terms of FID on state-of-the-art models for both conditional and unconditional settings on CIFAR-10, CelebA-HQ and ImageNet datasets. Moreover, we empirically show that LT-GAN helps in improving controlled image editing for CelebA-HQ and ImageNet over baseline models. We experimentally demonstrate that our proposed LT self-supervision task can be effectively combined with other state-of-the-art training techniques for added benefits. Consequently, we show that our approach achieves the new state-of-the-art FID score of 9.8 on conditional CIFAR-10 image generation."

tags:
- Generative adversarial networks
- Self supervised learning
- Image generation
- Latent transformations
- FID score
featured: false

links:
url_pdf: "https://arxiv.org/abs/2010.09893"
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

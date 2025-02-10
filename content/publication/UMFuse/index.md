---
title: "UMFuse: Unified Multi View Fusion for Human Editing applications"
authors:
- Rishabh Jain
- Mayur Hemani
- Duygu Ceylan
- Krishna Kumar Singh
- Jingwan Lu
- Mausoom Sarkar
- Balaji Krishnamurthy

date: "2023-08-02T00:00:00Z"
# doi: "10.18653/v1/2023.eacl-main.139"

publishDate: "2023-08-02T00:00:00Z"

publication_types: ["conference"]

publication: "IEEE/CVF International Conference on Computer Vision"
publication_short: "ICCV"

abstract: "Numerous pose-guided human editing methods have been explored by the vision community due to their extensive practical applications. However, most of these methods still use an image-to-image formulation in which a single image is given as input to produce an edited image as output. This objective becomes ill-defined in cases when the target pose differs significantly from the input pose. Existing methods then resort to in-painting or style transfer to handle occlusions and preserve content. In this paper, we explore the utilization of multiple views to minimize the issue of missing information and generate an accurate representation of the underlying human model. To fuse knowledge from multiple viewpoints, we design a multi-view fusion network that takes the pose key points and texture from multiple source images and generates an explainable perpixel appearance retrieval map. Thereafter, the encodings from a separate network (trained on a single-view human reposing task) are merged in the latent space. This enables us to generate accurate, precise, and visually coherent images for different editing tasks. We show the application of our network on two newly proposed tasks - Multi-view human reposing and Mix&Match Human Image generation. Additionally, we study the limitations of single-view editing and scenarios in which multi-view provides a better alternative."
summary: ""

tags:
- Computer Vision
- Human Reposing
- Mix and Match virtual Try On

featured: true


links:
url_pdf: "https://openaccess.thecvf.com/content/ICCV2023/html/Jain_UMFuse_Unified_Multi_View_Fusion_for_Human_Editing_Applications_ICCV_2023_paper.html"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: "https://mdsrlab.github.io/2023/08/13/UMFuse-ICCV.html"
url_slides: ""
url_source: ""
url_video: "https://www.youtube.com/watch?v=q8SS6zzSlr0"

image:
  caption: "Multi Image human reposing and mix and match virtual try on applications"
  focal_point: "UMFuse"
  preview_only: false
  alt_text: "Multi Image human reposing and mix and match virtual try on applications"

projects: []
slides: ""
---
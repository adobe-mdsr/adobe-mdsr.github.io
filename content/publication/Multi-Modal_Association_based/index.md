---
title: "Multi-Modal Association based Grouping for Form Structure Extraction"
authors:
- Milan Aggarwal
- Mausoom Sarkar
- Hiresh Gupta
- Balaji Krishnamurthy

date: "2020-01-01T00:00:00Z"
doi: ""

publishDate: "2020-01-01T00:00:00Z"

publication_types: ["conference"]

publication: "WACV"
publication_short: "WACV"

abstract: "Document structure extraction has been a widely researched area for decades. Recent work in this direction has been deep learning-based, mostly focusing on extracting structure using fully convolution NN through semantic segmentation. In this work, we present a novel multi-modal approach for form structure extraction. Given simple elements such as textruns and widgets, we extract higher-order structures such as TextBlocks, Text Fields, Choice Fields, and Choice Groups, which are essential for information collection in forms. To achieve this, we obtain a local image patch around each low-level element (reference) by identifying candidate elements closest to it. We process textual and spatial representation of candidates sequentially through a BiLSTM to obtain context-aware representations and fuse them with image patch features obtained by processing it through a CNN. Subsequently, the sequential decoder takes this fused feature vector to predict the association type between reference and candidates. These predicted associations are utilized to determine larger structures through connected components analysis. Experimental results show the effectiveness of our approach achieving a recall of 90.29%, 73.80%, 83.12%, and 52.72% for the above structures, respectively, outperforming semantic segmentation baselines significantly. We show the efficacy of our method through ablations, comparing it against using individual modalities. We also introduce our new rich human-annotated Forms Dataset."

summary: ""

tags:
- Through
- Semantic Segmentation
- Structure
- Structures
- Deep Learning
featured: false

links:
url_pdf: "https://openaccess.thecvf.com/content_WACV_2020/html/Aggarwal_Multi-Modal_Association_based_Grouping_for_Form_Structure_Extraction_WACV_2020_paper.html"
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

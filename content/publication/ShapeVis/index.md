---
title: "ShapeVis: High-dimensional Data Visualization at Scale"
authors:
- Nupur Kumari
- Siddarth R.
- Akash Rupela
- Piyush Gupta
- Balaji Krishnamurthy

date: "2020-01-01T00:00:00Z"
doi: ""

publishDate: "2020-01-01T00:00:00Z"

publication_types: ["conference"]

publication: "WWW"
publication_short: "WWW"

abstract: "We present ShapeVis, a scalable visualization technique for point cloud data inspired from topological data analysis. Our method captures the underlying geometric and topological structure of the data in a compressed graphical representation. Much success has been reported by the data visualization technique Mapper, that discreetly approximates the Reeb graph of a filter function on the data. However, when using standard dimensionality reduction algorithms as the filter function, Mapper suffers from considerable computational cost. This makes it difficult to scale to high-dimensional data. Our proposed technique relies on finding a subset of points called landmarks along the data manifold to construct a weighted witness-graph over it. This graph captures the structural characteristics of the point cloud, and its weights are determined using a Finite Markov Chain. We further compress this graph by applying induced maps from standard community detection algorithms. Using techniques borrowed from manifold tearing, we prune and reinstate edges in the induced graph based on their modularity to summarize the shape of data. We empirically demonstrate how our technique captures the structural characteristics of real and synthetic data sets. Further, we compare our approach with Mapper using various filter functions like t-SNE, UMAP, LargeVis and show that our algorithm scales to millions of data points while preserving the quality of data visualization."

tags: ["Shapevis", "Point cloud", "Topological data analysis", "Dimensionality reduction", "Graph compression"]
summary: ""

tags:
- Visualization
- Point cloud
- Topological data analysis
- Dimensionality reduction
- Community detection
featured: false

links:
url_pdf: "https://arxiv.org/abs/2001.05166"
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


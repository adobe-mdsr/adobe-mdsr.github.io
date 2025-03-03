---
title: "SARC: Soft Actor Retrospective Critic"
authors:
- Sukriti Verma
- Jayakumar Subramanian
- Ayush Chopra
- Nikaash Puri
- Mausoom Sarkar
- Piyush Gupta
- Balaji Krishnamurthy

date: "2022-01-01T00:00:00Z"
doi: ""

publishDate: "2022-01-01T00:00:00Z"

publication_types: ["conference"]

publication: "RLDM"
publication_short: "RLDM"

abstract: "The two-time scale nature of SAC, which is an actor-critic algorithm, is characterised by the fact that the critic estimate has not converged for the actor at any given time, but since the critic learns faster than the actor, it ensures eventual consistency between the two. Various strategies have been introduced in literature to learn better gradient estimates to help achieve better convergence. Since gradient estimates depend upon the critic, we posit that improving the critic can provide a better gradient estimate for the actor at each time. Utilizing this, we propose Soft Actor Retrospective Critic (SARC), where we augment the SAC critic loss with another loss term - retrospective loss - leading to faster critic convergence and consequently, better policy gradient estimates for the actor. An existing implementation of SAC can be easily adapted to SARC with minimal modifications. Through extensive experimentation and analysis, we show that SARC provides consistent improvement over SAC on benchmark environments. We plan to open-source the code and all experiment data at: this https URL."

summary: ""

tags:
- Critic
- Better
- Gradient
- Estimates
- Faster
featured: false

links:
url_pdf: "https://arxiv.org/abs/2306.16503"
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

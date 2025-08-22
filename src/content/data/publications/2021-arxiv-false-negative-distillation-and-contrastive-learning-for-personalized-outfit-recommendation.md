---
template: articles/publication
category: publication
status: published
date: 2021-10-13
title: False Negative Distillation and Contrastive Learning for Personalized Outfit Recommendation
slug: 2021-arxiv-false-negative-distillation-and-contrastive-learning-for-personalized-outfit-recommendation
summary: We propose False Negative Distillation and a contrastive learning framework with novel augmentations to address scalability and data sparsity in personalized outfit recommendation, achieving strong performance without exhaustive ranking.
cover: publication.jpg
image: 2021-arxiv-false-negative-distillation-and-contrastive-learning-for-personalized-outfit-recommendation.jpg
year: 2021
authors: Seongjae Kim, Jinseok Seol, Holim Lim, Sang-goo Lee
venue_type: Preprint
venue_name: arXiv Preprint
venue_short: arXiv
projects:
link: https://arxiv.org/abs/2110.06483
code:
---

Personalized outfit recommendation has recently been in the spotlight with the rapid growth of the online fashion industry. However, recommending outfits has two significant challenges that should be addressed. The first challenge is that outfit recommendation often requires a complex and large model that utilizes visual information, incurring huge memory and time costs. One natural way to mitigate this problem is to compress such a cumbersome model with knowledge distillation (KD) techniques that leverage knowledge from a pretrained teacher model. However, it is hard to apply existing KD approaches in recommender systems (RS) to the outfit recommendation because they require the ranking of all possible outfits while the number of outfits grows exponentially to the number of consisting clothing items. Therefore, we propose a new KD framework for outfit recommendation, called False Negative Distillation (FND), which exploits false-negative information from the teacher model while not requiring the ranking of all candidates. The second challenge is that the explosive number of outfit candidates amplifying the data sparsity problem, often leading to poor outfit representation. To tackle this issue, inspired by the recent success of contrastive learning (CL), we introduce a CL framework for outfit representation learning with two proposed data augmentation methods. Quantitative and qualitative experiments on outfit recommendation datasets demonstrate the effectiveness and soundness of our proposed methods.

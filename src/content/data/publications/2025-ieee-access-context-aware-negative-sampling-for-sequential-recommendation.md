---
template: articles/publication
category: publication
status: published
date: 2025-06-03
title: Context-aware Negative Sampling for Sequential Recommendation
slug: 2025-ieee-access-context-aware-negative-sampling-for-sequential-recommendation
summary: We propose two plug-and-play negative sampling methods, context-aware hard negative sampling and negative context sampling, that improve recommendation diversity by over 20% with minimal accuracy loss, leveraging context-dependent item distributions.
cover: publication.jpg
image: 2025-ieee-access-context-aware-negative-sampling-for-sequential-recommendation.jpg
year: 2025
authors: Jinseok Seol, Jaesik Choi
venue_type: Journal
venue_name: IEEE Access, volume 16, pp 97717-97736
venue_short: IEEE Access
projects:
link: https://ieeexplore.ieee.org/abstract/document/11021640
code: https://github.com/theeluwin/CaNS
---

Recommender systems have become essential in large-scale e-commerce and content platforms. While user preferences are crucial in generating recommendations, the context in which recommendations are made—such as time, location, and occasion—also plays a significant role. Over the past decades, context-aware models have been developed to address this. However, the use of context information in negative sampling remains less expored, despite the well-known impact of sampling strategies on recommendation performance. In this study, we first quantitatively demonstrate that item distributions vary significantly across different contexts. Based on this observation, we propose two novel negative sampling methods: context-aware hard negative item sampling and negative context sampling. These methods enhance recommendation diversity by more accurately reflecting context-dependent item distributions during training. To validate the effectiveness of the proposed methods, we apply them to a sequential recommendation model leveraging temporal context, where time information plays a critical role. The proposed methods are designed to be easily integrated into any sampling-based sequential recommendation model in a plug-and-play manner, and extensive experimental results on 10 real-world datasets demonstrate that the proposed methods significantly improve recommendation diversity, with an average increase of 20.65%, while incurring only a minor accuracy loss of 1.89%.

---
template: articles/publication
category: publication
status: published
date: 2025-02-24
title: Parameter-efficiently Leveraging Session Information in Deep Learning based Session-aware Sequential Recommendation
slug: 2025-ieee-access-parameter-efficiently-leveraging-session-information-in-deep-learning-based-session-aware-sequential-recommendation
summary: We propose three lightweight methods, session tokens, session segment embeddings, and temporal self-attention, to effectively incorporate session information into sequential recommendation models, achieving up to 10% improvement with minimal parameter overhead.
cover: publication.jpg
image: 2025-ieee-access-parameter-efficiently-leveraging-session-information-in-deep-learning-based-session-aware-sequential-recommendation.jpg
year: 2025
authors: Jinseok Seol, Youngrok Ko, Sang-goo Lee
venue_type: Journal
venue_name: IEEE Access, volume 13, pp 35555-35566
venue_short: IEEE Access
projects:
link: https://ieeexplore.ieee.org/abstract/document/10902109
code: https://github.com/theeluwin/session-aware-bert4rec
---

In recommender systems, leveraging user interaction history as sequential information has recently led to significant performance improvements. However, in many online services, user interactions are often grouped into sessions that inherently share user preferences, requiring a distinct approach from conventional sequence representation techniques. Existing studies have introduced various methods to integrate session information into sequential recommendation models, but most rely on complex network structures, such as hierarchical networks, or introduce substantial additional parameters. In this paper, we revisit the importance of incorporating session information in sequential recommendation models. We propose three methods to enhance recommendation performance by effectively utilizing session information while minimizing additional parameter overhead in deep learning-based sequential recommendation models: session token, session segment embeddings, and temporal self-attention. The proposing methods are designed to be easily integrated into both RNN-based and attention-based models. We demonstrate the effectiveness of the proposed methods through extensive experiments on real-world recommendation datasets, achieving up to a 10% performance improvement with only 1% additional parameters.

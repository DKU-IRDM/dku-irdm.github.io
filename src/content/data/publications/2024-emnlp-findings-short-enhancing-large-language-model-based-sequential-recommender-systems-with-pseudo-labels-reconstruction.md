---
template: articles/publication
category: publication
status: published
date: 2024-11-01
title: Enhancing Large Language Model Based Sequential Recommender Systems with Pseudo Labels Reconstruction
slug: 2024-emnlp-findings-short-enhancing-large-language-model-based-sequential-recommender-systems-with-pseudo-labels-reconstruction
summary: We propose ReLRec, a reconstruction-based LLM recommendation model that preserves language generation abilities while leveraging pseudo-labels from user reviews to enhance sequential recommendation performance.
cover: publication.jpg
image: 2024-emnlp-findings-short-enhancing-large-language-model-based-sequential-recommender-systems-with-pseudo-labels-reconstruction.jpg
year: 2024
authors: Hyunsoo Na, Minseok Gang, Youngrok Ko, Jinseok Seol, Sang-goo Lee
venue_type: Conference
venue_name: The 2024 Conference on Empirical Methods in Natural Language Processing
venue_short: EMNLP Findings Short
projects:
link: https://aclanthology.org/2024.findings-emnlp.423/
code:
---

Large language models (LLMs) are utilized in various studies, and they also demonstrate a potential to function independently as a recommendation model. Nevertheless, training sequences and text labels modifies LLMs’ pre-trained weights, diminishing their inherent strength in constructing and comprehending natural language sentences. In this study, we propose a reconstruction-based LLM recommendation model (ReLRec) that harnesses the feature extraction capability of LLMs, while preserving LLMs’ sentence generation abilities. We reconstruct the user and item pseudo-labels generated from user reviews, while training on sequential data, aiming to exploit the key features of both users and items. Experimental results demonstrate the efficacy of label reconstruction in sequential recommendation tasks.

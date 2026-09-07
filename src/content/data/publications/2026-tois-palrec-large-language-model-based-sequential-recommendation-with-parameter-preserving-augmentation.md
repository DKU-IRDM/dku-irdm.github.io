---
template: articles/publication
category: publication
status: published
date: 2026-09-03
title: PALRec - Large Language Model-Based Sequential Recommendation With Parameter-Preserving Augmentation
slug: 2026-tois-palrec-large-language-model-based-sequential-recommendation-with-parameter-preserving-augmentation
summary: We propose PALRec, which enhances LLM-based recommendation by integrating collaborative signals through lightweight modules while preserving the LLM’s parameters and pre-trained knowledge.
cover: publication.jpg
image: 2026-tois-palrec-large-language-model-based-sequential-recommendation-with-parameter-preserving-augmentation.jpg
year: 2026
authors: Hyunsoo Na, Minseok Gang, Sang-goo Lee, Jinseok Seol
venue_type: Journal
venue_name: ACM Transactions on Information Systems
venue_short: TOIS
projects:
link: https://dl.acm.org/doi/abs/10.1145/3842668
code:
---

Large Language Models (LLMs) have demonstrated remarkable general-purpose abilities across a wide range of domains, and these strengths have also been increasingly evidenced in recommender systems. However, existing methods that attempt to integrate collaborative signals into LLMs often fail to preserve their foundational knowledge. This loss is critical in text-rich recommendation, where robust semantic understanding is required to interpret user reviews and item profiles. We propose PALRec, a parameter-preserving augmentation framework that equips an LLM with recommendation capabilities while keeping its original parameters fixed. We first construct evidence-grounded user and item profiles from reviews and use them as concise pseudo-labels for reconstruction. We then introduce lightweight, trainable user and item embedding modules optimized with a multi-task objective that combines next-item prediction and profile reconstruction. These modules are trained jointly to align collaborative signals with the LLM’s semantic space without modifying the backbone. We also employ token-aware loss decomposition and frequency-aware reweighting to stabilize training and mitigate popularity bias. Experiments on public benchmarks show that PALRec consistently outperforms fully fine-tuned counterparts in recommendation accuracy while preserving the LLM’s pre-trained knowledge. This result highlights that maintaining the LLM’s semantic understanding is crucial for effectively exploiting textual information in recommender systems.

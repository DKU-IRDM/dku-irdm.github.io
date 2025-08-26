---
template: articles/publication
category: publication
status: published
date: 2025-11-12
title: On the Relationship between Populated Regions and Adversarial Robustness in Deep Neural Networks
slug: 2025-icdm-short-on-the-relationship-between-populated-regions-and-adversarial-robustness-in-deep-neural-networks
summary: We introduce the Populated Region Set (PRS) to analyze internal properties of DNNs, show that a low PRS ratio strongly correlates with adversarial robustness, and propose a PRS regularizer to enhance robustness without adversarial training.
cover: publication.jpg
image: 2025-icdm-short-on-the-relationship-between-populated-regions-and-adversarial-robustness-in-deep-neural-networks.jpg
year: 2025
authors: Seongjin Park, Haedong Jeong, Tair Djanibekov, Giyoung Jeon, Jinseok Seol, and Jaesik Choi
venue_type: Conference
venue_name: The 25th IEEE International Conference on Data Mining
venue_short: ICDM short
projects:
link:
code:
---

In general, deep neural networks (DNNs) are evaluated by the generalization performance measured on unseen data excluded from the training phase. Along with the development of DNNs, the generalization performance converges to the state-of-the-art and it becomes difficult to evaluate DNNs solely based on this metric. The robustness against adversarial attack has been used as an additional metric to evaluate DNNs by measuring their vulnerability. However, few studies have been performed to analyze the adversarial robustness in terms of the geometry in DNNs. In this work, we perform an empirical study to analyze the internal properties of DNNs that affect model robustness under adversarial attacks. In particular, we propose the novel concept of the populated region get (PRS), where training samples are populated more frequently, to represent the internal properties of DNNs in a practical setting. From systematic experiments with the proposed concept, we provide empirical evidence to validate that a low PRS ratio has a strong relationship with the adversarial robustness of DNNs. We also devise PRS regularizer leveraging the characteristics of PRS to improve the adversarial robustness without adversarial training.

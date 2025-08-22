---
template: articles/publication
category: publication
status: published
date: 2021-08-19
title: Masked Contrastive Learning for Anomaly Detection
slug: 2021-ijcai-masked-contrastive-learning-for-anomaly-detection
summary: We propose masked contrastive learning and self-ensemble inference, two task-specific self-supervised methods tailored for anomaly detection, that significantly outperform prior state-of-the-art on benchmark datasets.
cover: publication.jpg
image: 2021-ijcai-masked-contrastive-learning-for-anomaly-detection.jpg
year: 2021
authors: Hyunsoo Cho, Jinseok Seol, Sang-goo Lee
venue_type: Conference
venue_name: The Thirtieth International Joint Conference on Artificial Intelligence
venue_short: IJCAI
projects:
link: https://www.ijcai.org/proceedings/2021/0198.pdf
code:
---

Detecting anomalies is one fundamental aspect of a safety-critical software system, however, it remains a long-standing problem. Numerous branches of works have been proposed to alleviate the complication and have demonstrated their efficiencies. In particular, self-supervised learning based methods are spurring interest due to their capability of learning diverse representations without additional labels. Among self-supervised learning tactics, contrastive learning is one specific framework validating their superiority in various fields, including anomaly detection. However, the primary objective of contrastive learning is to learn task-agnostic features without any labels, which is not entirely suited to discern anomalies. In this paper, we propose a task-specific variant of contrastive learning named masked contrastive learning, which is more befitted for anomaly detection. Moreover, we propose a new inference method dubbed self-ensemble inference that further boosts performance by leveraging the ability learned through auxiliary self-supervision tasks. By combining our models, we can outperform previous state-of-the-art methods by a significant margin on various benchmark datasets.

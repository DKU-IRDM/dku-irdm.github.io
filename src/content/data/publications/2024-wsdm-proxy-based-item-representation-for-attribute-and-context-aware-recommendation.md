---
template: articles/publication
category: publication
status: published
date: 2024-03-04
title: Proxy-based Item Representation for Attribute and Context-aware Recommendation
slug: 2024-wsdm-proxy-based-item-representation-for-attribute-and-context-aware-recommendation
summary: We propose a proxy-based item representation method that compositionally encodes items using shared proxy embeddings informed by attributes and context, significantly improving recommendation accuracy, especially for infrequent items, while reducing parameter usage.
cover: publication.jpg
image: 2024-wsdm-proxy-based-item-representation-for-attribute-and-context-aware-recommendation.jpg
year: 2024
authors: Jinseok Seol, Minseok Gang, Sang-goo Lee, Jaehui Park
venue_type: Conference
venue_name: The 17th ACM International Conference on Web Search and Data Mining
venue_short: WSDM
projects:
link: https://dl.acm.org/doi/abs/10.1145/3616855.3635824
code: https://github.com/theeluwin/ProxyRCA
---

Neural network approaches in recommender systems have shown remarkable success by representing a large set of items as a learnable vector embedding table. However, infrequent items may suffer from inadequate training opportunities, making it difficult to learn meaningful representations. We examine that in attribute and context-aware settings, the poorly learned embeddings of infrequent items impair the recommendation accuracy. To address such an issue, we propose a proxy-based item representation that allows each item to be expressed as a weighted sum of learnable proxy embeddings. Here, the proxy weight is determined by the attributes and context of each item and may incorporate bias terms in case of frequent items to further reflect collaborative signals. The proxy-based method calculates the item representations compositionally, ensuring each representation resides inside a well-trained simplex and, thus, acquires guaranteed quality. Additionally, that the proxy embeddings are shared across all items allows the infrequent items to borrow training signals of frequent items in a unified model structure and end-to-end manner. Our proposed method is a plug-and-play model that can replace the item encoding layer of any neural network-based recommendation model, while consistently improving the recommendation performance with much smaller parameter usage. Experiments conducted on real-world recommendation benchmark datasets demonstrate that our proposed model outperforms state-of-the-art models in terms of recommendation accuracy by up to 17% while using only 10% of the parameters.

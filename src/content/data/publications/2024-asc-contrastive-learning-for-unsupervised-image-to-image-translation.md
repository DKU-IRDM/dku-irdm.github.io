---
template: articles/publication
category: publication
status: published
date: 2024-01-01
title: Contrastive Learning for Unsupervised Image-to-image Translation
slug: 2024-asc-contrastive-learning-for-unsupervised-image-to-image-translation
summary: We propose a novel unsupervised image-to-image translation method that learns visual similarity without predefined domains, achieving significantly improved FID and translation accuracy while reducing annotation costs.
cover: publication.jpg
image: 2024-asc-contrastive-learning-for-unsupervised-image-to-image-translation.jpg
year: 2024
authors: Hanbit Lee, Jinseok Seol, Sang-goo Lee, Jaehui Park, Junho Shim
venue_type: Journal
venue_name: Applied Soft Computing, volume 151, pp 111170
venue_short: ASC
projects:
link: https://www.sciencedirect.com/science/article/abs/pii/S1568494623011882
code:
---

Image-to-image translation (I2I) aims to learn a mapping function to transform images into different styles or domains while preserving their key structures. Typically, I2I models require manually defined image domains as a training set to learn the visual differences among the image domains and achieve the ability to translate images across them. However, constructing such multi-domain datasets on a large scale requires expensive data collection and annotation processes. Moreover, if the target domain changes or is expanded, a new dataset should be collected, and the model should be retrained. To address these challenges, this article presents a novel unsupervised I2I method that does not require manually defined image domains. The proposed method automatically learns the visual similarity between individual samples and leverages the learned similarity function to transfer a specific style or appearance across images. Therefore, the developed method does not rely on cost-intensive manual domains or unstable clustering results, leading to improved translation accuracy at minimal cost. For quantitative evaluation, we implemented a state-of-the-art I2I models and performed image transformation on the same input image using the baselines and our method. The image quality was then assessed using two quantitative metrics: Frechet inception distance (FID) and translation accuracy. The proposed method exhibited significant improvements in image quality and translation accuracy compared with the latest unsupervised I2I methods. Specifically, the developed technique achieved a 25% and 19% improvement over the best-performing unsupervised baseline in terms of FID and translation accuracy, respectively. Furthermore, this approach demonstrated performance nearly comparable to those of supervised learning-based methods trained using manually collected and constructed domains.

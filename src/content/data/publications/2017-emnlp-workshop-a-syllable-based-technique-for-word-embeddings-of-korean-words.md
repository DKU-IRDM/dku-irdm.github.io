---
template: articles/publication
category: publication
status: published
date: 2017-08-05
title: A Syllable-based Technique for Word Embeddings of Korean Words
slug: 2017-emnlp-workshop-a-syllable-based-technique-for-word-embeddings-of-korean-words
summary: We propose a CNN-based syllable-level embedding model for Korean that captures morphological features and alleviates the OOV problem better than Skip-gram.
cover: publication.jpg
image: 2017-emnlp-workshop-a-syllable-based-technique-for-word-embeddings-of-korean-words.jpg
year: 2017
authors: Sanghyuk Choi, Taeuk Kim, Jinseok Seol, Sang-goo Lee
venue_type: Workshop
venue_name: The First Workshop on Subword and Character Level Models in NLP
venue_short: EMNLP Workshop
projects:
link: https://aclanthology.org/W17-4105/
code:
---

Word embedding has become a fundamental component to many NLP tasks such as named entity recognition and machine translation. However, popular models that learn such embeddings are unaware of the morphology of words, so it is not directly applicable to highly agglutinative languages such as Korean. We propose a syllable-based learning model for Korean using a convolutional neural network, in which word representation is composed of trained syllable vectors. Our model successfully produces morphologically meaningful representation of Korean words compared to the original Skip-gram embeddings. The results also show that it is quite robust to the Out-of-Vocabulary problem.

---
template: articles/publication
category: publication
status: published
date: 2016-12-01
title: "lexrankr: LexRank 기반 한국어 다중 문서 요약"
slug: 2016-kcc-lexrankr-lexrank-based-korean-multi-document-summarization
summary: 본 연구는 LexRank 알고리즘을 한국어에 적합하도록 구현한 파이썬 패키지 lexrankr에 대해 다룬다.
cover: publication.jpg
image:
year: 2016
authors: 설진석, 이상구
venue_type: Conference
venue_name: 한국정보과학회 2016 동계학술대회
venue_short: KCC
projects:
link: https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE07017863
code: https://github.com/TA-wannabe/Accelerator
---

본 논문에선 LexRank 알고리즘을 한국어에 적합하도록 구현한 파이썬 패키지 lexrankr 에 대해 기술한다. LexRank 알고리즘은 TextRank 와 비슷하게, 문서 내의 각 문장들을 노드로, 문장들 간 유사도를 간선의 값으로 그래프를 만든 후 PageRank 를 적용해서 중요한 문장을 추출해내는 추출 기반 문서 요약 알고리즘이다. 본 논문에선 LexRank 알고리즘을 비롯한 추출 기반 문서 요약 방법론들을 적용하여 한국어에 적합하도록 파이썬 패키지로써 구현한 방법을 자세히 기술한다. 긴 문서를 주제별로 요약하기 위해새로운 유사도 함수를 제안하며, 원하는 축약 정도를 맞추기 위한 클러스터 탐색 방법 역시 제안한다. 편리하게 사용할 수 있도록 패키지화 되어있으며, 오픈소스의 형태로 개발되었다.

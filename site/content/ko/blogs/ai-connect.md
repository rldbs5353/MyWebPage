---
title: "AI 커넥트 프로젝트"
date: 2026-06-30
draft: false
author: "엄기윤"
# TODO(엄기윤): 아래 본문은 AI가 작성한 초안입니다. 실제 진행 기간·팀 구성·데이터·모델·결과로 꼭 수정하세요.
tags:
  - AI
  - Python
  - 팀 프로젝트
image: /images/projects/ai-connect.svg
description: "Python으로 데이터 전처리부터 분류 모델 학습, 결과 분석까지 진행한 팀 프로젝트"
toc: true
---

## 프로젝트 개요

| 항목 | 내용 |
| --- | --- |
| 활동명 | AI 커넥트 프로젝트 |
| 형태 | 팀 프로젝트 |
| 사용 기술 | Python, pandas, scikit-learn, Jupyter Notebook |
| 나의 역할 | 데이터 전처리, 모델 학습 및 성능 비교 |

## 목적

인공지능 수업에서 배운 이론을 **실제 데이터에 직접 적용해 보는 것**이 목표였습니다.
"모델이 데이터로부터 어떻게 학습하는가"를 코드로 확인하고, 데이터를 준비하는 과정부터 결과를 해석하는 과정까지 머신러닝 프로젝트의 전체 흐름을 경험하고자 했습니다.

## 나의 역할

- **데이터 전처리**: 결측치 처리, 범주형 데이터 인코딩, 정규화
- **모델 학습**: 여러 분류 모델(로지스틱 회귀, 결정 트리, 랜덤 포레스트)을 학습하고 비교
- **결과 정리**: 정확도·혼동 행렬로 성능을 비교하고 발표 자료 작성에 참여

## 진행 과정

1. **주제 선정 및 데이터 확보** — 팀원들과 회의하여 공개 데이터셋을 선택했습니다.
2. **탐색적 데이터 분석(EDA)** — pandas로 데이터 분포와 결측치를 확인하고 시각화했습니다.
3. **전처리** — 학습에 방해가 되는 값을 정리하고, 학습용/검증용 데이터로 나눴습니다.
4. **모델 학습 및 비교** — scikit-learn으로 여러 모델을 학습시키고 같은 기준으로 평가했습니다.
5. **결과 분석 및 발표** — 어떤 특징(feature)이 결과에 큰 영향을 주는지 분석하고 팀 발표를 진행했습니다.

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("정확도:", accuracy_score(y_test, model.predict(X_test)))
```

## 결과

- 여러 모델 중 **랜덤 포레스트**가 가장 안정적인 성능을 보였습니다.
- 전처리를 거친 뒤 모델 성능이 눈에 띄게 좋아지는 것을 확인했습니다.
- 팀 발표를 무사히 마쳤고, 코드와 분석 결과를 정리해 공유했습니다.

## 배운 점

- 좋은 모델보다 **좋은 데이터 준비**가 결과에 더 큰 영향을 준다는 것을 체감했습니다.
- 팀원과 역할을 나누고 Git으로 코드를 공유하면서 협업 방식을 익혔습니다.
- 다음에는 PyTorch로 딥러닝 모델을 직접 구현해 보고 싶습니다.

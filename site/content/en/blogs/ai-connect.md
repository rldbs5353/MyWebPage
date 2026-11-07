---
title: "AI Connect Project"
date: 2026-06-30
draft: false
author: "Kiyun Eom"
# TODO: This is an AI-written draft. Update it with the real period, team, data, model and results.
tags:
  - AI
  - Python
  - Team Project
image: /images/projects/ai-connect.svg
description: "A team project covering data preprocessing, classification model training, and result analysis with Python"
toc: true
---

## Overview

| Item | Details |
| --- | --- |
| Activity | AI Connect Project |
| Type | Team project |
| Tech | Python, pandas, scikit-learn, Jupyter Notebook |
| My role | Data preprocessing, model training and comparison |

## Purpose

The goal was to **apply the theory from my AI class to real data**.
I wanted to see in code how a model learns from data, and to experience the whole flow of a machine learning project — from preparing data to interpreting results.

## My Role

- **Data preprocessing**: handling missing values, encoding categorical data, normalization
- **Model training**: training and comparing several classifiers (logistic regression, decision tree, random forest)
- **Reporting**: comparing performance with accuracy and confusion matrices, and helping prepare the presentation

## Process

1. **Topic and data** — chose a public dataset together with the team.
2. **Exploratory data analysis** — checked distributions and missing values with pandas and visualized them.
3. **Preprocessing** — cleaned problematic values and split the data into training and validation sets.
4. **Training and comparison** — trained several models with scikit-learn and evaluated them on the same criteria.
5. **Analysis and presentation** — analyzed which features influenced the results most and presented as a team.

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
```

## Results

- Among the models, **random forest** showed the most stable performance.
- Performance improved noticeably after preprocessing.
- We completed the team presentation and shared the code and analysis.

## What I Learned

- **Good data preparation** matters more than picking a fancy model.
- I learned how to split roles and share code with Git in a team.
- Next, I want to implement deep learning models myself with PyTorch.

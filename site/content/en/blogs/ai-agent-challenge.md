---
title: "2026 AI Agent Challenge"
date: 2026-07-31
draft: false
author: "Kiyun Eom"
tags:
  - AI
  - Planning
  - Development Project
image: /images/projects/ai-agent-challenge.png
description: "AI agent planning & development project · Mentoring by Team NAVER developers · Demo Day presentation and exhibition"
toc: true
---

## Overview

| Item | Details |
| --- | --- |
| Activity | 2026 AI Agent Challenge |
| Service | **Review Manager AI** — a review management web page for small business owners |
| Type | Individual development project |
| Period | Jul 6 – Jul 31, 2026 (4 weeks, online full-time) |
| Status | **Completed (certificate received)** |
| Tech | Using AI agents (Claude Code) |
| My role | Web page planning and development |

## Purpose

This program was designed to help students plan and build real AI agents themselves, and to develop their AI and software development skills through mentoring by Team NAVER developers and participation in a Demo Day.

### The problem

Owners of cafés and restaurants get new reviews every day, and I started from three difficulties they face:

1. **Choosing a reply tone** — deciding how to reply to each review takes time, every single time.
2. **Missing repeated complaints** — the same complaint (e.g. "the wait was too long") keeps coming back, but it is easy to miss the pattern when reading reviews one by one.
3. **Hard to prioritize** — as reviews pile up, it gets harder to decide what to take care of first.

### Goal

Build a review management tool where owners simply **paste customer reviews** to get sentiment analysis, keyword extraction, repeated-issue detection and three reply drafts, and see an **overall analysis and monthly statistics** based on an AI score for each review.

## My Role

I took part as an **individual project** and did **the whole process from planning to development on my own**.

- **Planning**: defined how users would use the AI agent, and the screens and features it needed.
- **Development**: implemented the web page based on the plan and connected the AI agent's features to the UI.
- **Using AI agents**: actively used AI agents during development to write code and fix errors faster.
- **Applying feedback**: improved the plan and the web page myself based on mentors' feedback.

## Process

The program was a summer camp run by the NAVER Connect Foundation and Seoul National University, held online full-time from **July 6 to July 31, 2026**.

1. **Learning AI agents** — learned the concepts and how to design and build AI agents through hands-on practice.
2. **Topic and planning** — decided on my own which problem to solve with an AI agent and planned the service's core features.
3. **Web page design and development** — designed screens based on the service flow and developed the web page using AI agents.
4. **Mentoring** — reviewed and improved my plan and implementation with mentoring from Team NAVER developers.
5. **Demo Day** — presented and exhibited the service at the Demo Day held at NAVER 1784.

### Why I chose Claude Code

Among several AI agents, I chose **Claude Code** as my development tool.

- I judged that it writes more complete code and has better features than other agents.
- Since I had to do everything from planning to development alone, I expected it to help a lot not only with writing code but also with fixing errors.

## Output: Review Manager AI screens

### 1) Tool — paste reviews

![Review Manager AI tool screen: an input box for pasting up to 15 reviews, one per line, with an Analyze button and a result preview](/images/projects/review-manager/tool.webp)

Owners copy reviews from delivery apps or map services and paste them **one per line, up to 15 at a time**. I added **sample buttons** such as "long wait complaint" and "friendliness praise" so first-time users can try it right away.

### 2) How it works — analysis and reply drafts

![Review Manager AI guide screen: a negative review tagged with taste and wait-time keywords, an improvement suggestion, and reply drafts in polite and friendly tones](/images/projects/review-manager/guide.webp)

Each review gets a **sentiment (positive / negative / neutral) and keywords** (e.g. #taste, #wait time), an **improvement suggestion**, and **three reply drafts in different tones** such as polite and friendly. The owner can copy the one they like.

### 3) Overall analysis — statistics and AI insight

![Review Manager AI overall analysis screen: 10 reviews analyzed, average attention score 49, 40% positive, keyword bar chart, monthly sentiment trend and an AI insight](/images/projects/review-manager/analysis.webp)

It collects all analyzed reviews and shows the **sentiment distribution, average attention score, frequent keywords and monthly sentiment trend**. The screen above is the result for 10 sample reviews; the AI insight points out **repeated problems and what to fix first**, e.g. "wait-time complaints (4 cases) are the most serious issue".

### Evidence link

- [AI Agent Challenge 2026 project hub](https://connect-aiagentchallenge-26-1.github.io/hub/) — the official page collecting participants' projects

## Results

- Completed **Review Manager AI from planning to development on my own** in four weeks.
- Presented and exhibited the result at the **NAVER 1784 Demo Day**.
- Received an official certificate of completion from the NAVER Connect Foundation and Seoul National University.

## What I Learned

- By planning and building an AI agent myself, I experienced **the whole process of turning AI into a service**.
- AI agents speed up implementation, but **deciding what to build and verifying the result are still up to people**.
- Handling both planning and development alone taught me the importance of **managing time and setting priorities**.
- Mentoring showed me that in practice, **the user's perspective** matters as much as implementing features.

## Limitations and Next Steps

| Limitation found | Next improvement |
| --- | --- |
| Analysis history is **stored only in the current browser**, so the statistics are not available on other devices. | Save each logged-in user's history **on a server** so the same statistics appear on any device |
| Only **up to 15 reviews** can be analyzed at once, so busy stores have to paste reviews in several batches. | Allow continuous batches or uploading a file at once |
| Reviews without specific expressions are grouped under **#general**, which makes it hard to know what to improve. | Refine the keyword categories and **verify accuracy myself** by comparing results with real reviews |

Next, I want to study how agents work in more depth and implement these improvements with an AI agent I design myself.

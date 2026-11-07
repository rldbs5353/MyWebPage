---
title: "Building a Portfolio Site with Hugo"
date: 2026-11-07
draft: false
author: "Kiyun Eom"
tags:
  - Hugo
  - GitHub Actions
  - Class Assignment
image: /images/projects/portfolio.svg
description: "How I built a personal portfolio with the Hugo Profile theme and deployed it to GitHub Pages automatically"
toc: true
---

## Overview

| Item | Details |
| --- | --- |
| Activity | Hugo portfolio site (class assignment) |
| Tech | Hugo 0.143.0 (extended), Hugo Profile theme, Git, GitHub Actions, GitHub Pages |
| Repository | [rldbs5353/MyWebPage](https://github.com/rldbs5353/MyWebPage) |
| My role | Solo work (theme selection, configuration, content, deployment, verification) |

## Purpose

To build a **personal portfolio site** where I can introduce myself and record my activities,
and to learn the **build and deployment process** with a static site generator (Hugo), Git and GitHub.

## Process

1. **Choosing a theme** — picked *Hugo Profile* from Hugo Themes because it has about, projects and blog sections.
2. **Connecting the repository** — connected the theme to my GitHub repository `MyWebPage`.
3. **Automatic deployment** — set up a workflow so that every push to `main` builds the site with Hugo in GitHub Actions and deploys it to GitHub Pages.
4. **Replacing content** — removed all of the theme's sample data and put my own information in `hugo.yaml`.
5. **Multilingual setup** — Korean is the default language and the English pages live under `/en/`, with a language switcher.
6. **Local verification** — previewed with `hugo server` and checked that menus, links, search and dark mode work.

## Results

- The site runs at `https://rldbs5353.github.io/MyWebPage/`.
- Every push rebuilds and redeploys it automatically.
- The introduction and activities are available in both Korean and English.

## What I Learned

- A single config file (`hugo.yaml`) can change the structure of the whole site.
- When deploying under a sub-path (`/MyWebPage/`), `baseURL` and image/link paths need care.
- Even when using AI for configuration and debugging, I have to build and check the result myself.

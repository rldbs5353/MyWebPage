---
title: "Hugo로 포트폴리오 사이트 만들기"
date: 2026-11-07
draft: false
author: "엄기윤"
tags:
  - Hugo
  - GitHub Actions
  - 수업 실습
image: /images/projects/portfolio.svg
description: "Hugo Profile 테마로 개인 포트폴리오를 만들고 GitHub Pages에 자동 배포한 과정"
toc: true
---

## 개요

| 항목 | 내용 |
| --- | --- |
| 활동명 | Hugo 포트폴리오 사이트 제작 (수업 과제) |
| 사용 기술 | Hugo 0.143.0 (extended), Hugo Profile 테마, Git, GitHub Actions, GitHub Pages |
| 저장소 | [rldbs5353/MyWebPage](https://github.com/rldbs5353/MyWebPage) |
| 나의 역할 | 개인 작업 (테마 선정, 설정, 콘텐츠 작성, 배포, 검증) |

## 목적

나를 소개하고 활동을 정리해 둘 수 있는 **개인 포트폴리오 사이트**를 직접 만들고,
정적 사이트 생성기(Hugo)와 Git·GitHub를 이용한 **빌드·배포 과정**을 익히는 것이 목적입니다.

## 진행 과정

1. **테마 선정** — Hugo Themes에서 자기소개·프로젝트·블로그 섹션이 모두 있는 *Hugo Profile* 테마를 골랐습니다.
2. **저장소 연결** — 테마를 내려받아 GitHub 저장소 `MyWebPage`에 연결했습니다.
3. **자동 배포 설정** — `main` 브랜치에 push하면 GitHub Actions가 Hugo로 사이트를 빌드하고 GitHub Pages에 배포하도록 워크플로를 구성했습니다.
4. **콘텐츠 교체** — 테마의 예시 데이터(가상 인물, 예시 글, 예시 이미지)를 모두 지우고 `hugo.yaml`에 내 정보를 넣었습니다.
5. **다국어 설정** — 한국어를 기본 언어로, 영어 페이지를 `/en/`에 두고 언어 전환 메뉴로 오갈 수 있게 했습니다.
6. **로컬 검증** — `hugo server`로 미리 보면서 메뉴·링크·검색·다크 모드가 동작하는지 확인했습니다.

## 결과

- `https://rldbs5353.github.io/MyWebPage/` 에서 사이트가 동작합니다.
- push할 때마다 자동으로 다시 빌드·배포됩니다.
- 한국어/영어 두 언어로 자기소개와 활동 기록을 볼 수 있습니다.

## 배운 점

- 설정 파일 하나(`hugo.yaml`)로 사이트 전체 구조를 바꿀 수 있다는 점이 인상적이었습니다.
- GitHub Pages처럼 하위 경로(`/MyWebPage/`)에 배포할 때는 `baseURL`과 이미지·링크 경로를 신경 써야 한다는 것을 알게 되었습니다.
- AI를 활용해 설정과 오류 분석을 하면서도, 결과가 실제로 맞는지는 직접 빌드하고 확인해야 한다는 것을 느꼈습니다.

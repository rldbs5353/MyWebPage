# 엄기윤 포트폴리오 사이트 (MyWebPage)

전북대학교 컴퓨터인공지능학부 엄기윤의 개인 소개 웹사이트입니다. 2026학년도 초급프로젝트 과제 1로 만들었습니다.

- **공개 사이트**: <https://rldbs5353.github.io/MyWebPage/> (한국어) · <https://rldbs5353.github.io/MyWebPage/en/> (English)
- **저장소**: <https://github.com/rldbs5353/MyWebPage>
- **배포 기록 (GitHub Actions)**: <https://github.com/rldbs5353/MyWebPage/actions>
- **사용 테마**: [Hugo Profile](https://github.com/gurusabarish/hugo-profile) (MIT License)

---

## 1. 필요한 도구와 버전

| 도구 | 버전 | 용도 |
| --- | --- | --- |
| Hugo **extended** | **0.143.0** | 사이트 빌드 (배포 워크플로와 같은 버전) |
| Python | 3.12 (Actions) / 3.14 (작성자 PC에서 확인) | 배포용 빌드 스크립트 `.github/pages_build.py` 실행 |
| Git | 2.x | 소스 관리, push |
| 웹 브라우저 | 최신 Chrome / Edge | 결과 확인 |

> 테마는 `site/themes/template/`에 저장소와 함께 들어 있어, 따로 내려받거나 `git submodule`을 설정할 필요가 없습니다.

## 2. 설치

### Windows (PowerShell)

```powershell
# Hugo extended 0.143.0 내려받기 → %LOCALAPPDATA%\Programs\hugo 에 설치
$dir = "$env:LOCALAPPDATA\Programs\hugo"
New-Item -ItemType Directory -Force $dir | Out-Null
Invoke-WebRequest "https://github.com/gohugoio/hugo/releases/download/v0.143.0/hugo_extended_0.143.0_windows-amd64.zip" -OutFile "$env:TEMP\hugo.zip"
Expand-Archive "$env:TEMP\hugo.zip" -DestinationPath $dir -Force
# 사용자 PATH에 추가 (새 터미널부터 적용)
[Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path','User') + ";$dir", 'User')
hugo version   # hugo v0.143.0-...+extended 가 나오면 성공
```

### macOS / Linux

```bash
# 예: Linux amd64
curl -L https://github.com/gohugoio/hugo/releases/download/v0.143.0/hugo_extended_0.143.0_linux-amd64.tar.gz | tar -xz
sudo mv hugo /usr/local/bin/
hugo version
```

### 저장소 받기

```bash
git clone https://github.com/rldbs5353/MyWebPage.git
cd MyWebPage
```

## 3. 로컬에서 확인하기

### 미리보기 (수정하면서 확인)

```powershell
# Windows: 저장소 루트에서
.\preview.ps1
```

```bash
# macOS / Linux 또는 직접 실행
cd site
hugo server --baseURL http://localhost:1313/ --appendPort=false --renderToMemory
```

브라우저에서 <http://localhost:1313/> (영어: `/en/`)을 엽니다. 파일을 저장하면 바로 반영되고, `Ctrl+C`로 종료합니다.

> `baseURL`이 `/MyWebPage/` 하위 경로라서, 로컬에서는 루트 주소(`localhost:1313/`)로 띄워야 이미지 경로가 맞습니다.

### 배포와 같은 방식으로 빌드 (결과 검사용)

```bash
# 저장소 루트에서 실행 → public/ 폴더에 배포될 결과물 생성
python .github/pages_build.py --build
```

GitHub Actions가 실행하는 것과 같은 스크립트이며, `/MyWebPage/` 하위 경로에 맞게 링크·이미지 주소를 보정합니다.
**미리보기 서버가 켜져 있으면 빌드 잠금 파일(`.hugo_build.lock`) 때문에 이 명령이 멈추므로, 먼저 미리보기를 종료하세요.**

### 빌드 결과 검사

```bash
python tools/check_links.py   # 깨진 내부 링크·이미지, /MyWebPage/ 경로 누락, localhost·PC 경로, 테마 예시 문구
python tools/check_a11y.py    # lang, 페이지당 h1, 이미지 alt, 아이콘 링크 이름, href="#"
```

둘 다 문제가 없으면 `문제 0건`을 출력하고 종료 코드 0을 돌려줍니다. GitHub Actions도 빌드 직후 같은 두 검사를 실행하며, 하나라도 실패하면 **배포하지 않습니다**.

## 4. 내용 수정 위치

| 바꿀 내용 | 파일 |
| --- | --- |
| 첫 화면 소개, 자기소개, 기술, 학력, 대표 활동 카드, 연락처 (한국어) | `site/hugo.yaml`의 `params:` 아래 |
| 위 내용의 영어 버전 | `site/hugo.yaml`의 `languages.en.params:` 아래 |
| 상단 메뉴 | `site/hugo.yaml`의 `languages.*.menu.main` |
| 활동 글 (한국어 / 영어) | `site/content/ko/blogs/*.md` / `site/content/en/blogs/*.md` |
| 이미지 | `site/static/images/` (글에서는 `/images/...` 경로로 사용) |
| 한국어 화면 문구 (메뉴 이름 등) | `site/i18n/ko.toml` |
| 테마 레이아웃 덮어쓰기 | `site/layouts/` (같은 경로의 테마 파일 대신 사용됨) |
| 추가 CSS | `site/static/css/custom.css` |
| 배포 워크플로 | `.github/workflows/hugo-pages.yml` |

## 5. 수정 후 배포하고 확인하는 방법

1. 위 파일을 수정하고 로컬 미리보기로 확인합니다.
2. 커밋하고 `main` 브랜치에 push 합니다.
   ```bash
   git add <수정한 파일>
   git commit -m "무엇을 왜 바꿨는지"
   git push origin main
   ```
3. <https://github.com/rldbs5353/MyWebPage/actions> 에서 **Deploy Hugo to GitHub Pages** 실행이 자동으로 시작되고, `build`와 `deploy`가 모두 초록색(성공)이 되는지 확인합니다. (보통 1분 내외)
   - `build` 안의 **Check links and asset paths**, **Check basic accessibility** 단계 로그에 `문제 0건`이 찍혀야 합니다. 실패하면 로그에 문제가 된 페이지와 주소가 표시됩니다.
4. <https://rldbs5353.github.io/MyWebPage/> 를 새로고침(`Ctrl+F5`)해 변경 내용이 반영됐는지 확인합니다.

> GitHub 저장소 **Settings → Pages → Build and deployment → Source**는 **GitHub Actions**로 설정되어 있어야 합니다.

## 6. 폴더 구조

```text
.
├── .github/
│   ├── workflows/hugo-pages.yml   # main push 시 빌드·배포 (Hugo 0.143.0 지정)
│   └── pages_build.py             # 수업 제공 빌드 스크립트 (경로 보정 포함)
├── site/                          # 실제 사이트
│   ├── hugo.yaml                  # 사이트 설정과 소개 내용
│   ├── pages.json                 # 배포용 baseURL 설정 (스크립트가 생성)
│   ├── content/ko, content/en     # 언어별 글
│   ├── i18n/ko.toml               # 한국어 화면 문구
│   ├── layouts/                   # 테마 덮어쓰기 (접근성 개선)
│   ├── static/                    # 이미지, 추가 CSS
│   └── themes/template/           # Hugo Profile 테마 원본
├── tools/
│   ├── check_links.py             # 빌드 결과 링크·자산 경로 검사
│   ├── check_a11y.py              # 빌드 결과 기본 접근성 검사
│   └── make_favicon.py            # 사이트 아이콘(fav.png) 생성
├── preview.ps1                    # 로컬 미리보기 실행 스크립트
├── AI_LOG.md                      # AI 활용 기록
└── README.md
```

## 7. 출처와 이용 조건

### 테마와 라이브러리

| 자료 | 출처 | 이용 조건 | 위치 |
| --- | --- | --- | --- |
| Hugo Profile 테마 | <https://github.com/gurusabarish/hugo-profile> (Gurusabarish) | MIT License — 원문 [`site/themes/template/LICENSE`](site/themes/template/LICENSE), [`LICENSE`](LICENSE) 유지 | `site/themes/template/` |
| Bootstrap 5 | <https://getbootstrap.com> (테마에 포함) | MIT License | `site/themes/template/static/bootstrap-5/` |
| Font Awesome 6 Free | <https://fontawesome.com> (테마에 포함) | 아이콘 CC BY 4.0, 코드 MIT | `site/themes/template/static/fontawesome-6/` |
| Viewer.js | <https://github.com/fengyuanchen/viewerjs> (테마에 포함) | MIT License | `site/themes/template/static/viewer/` |
| Google Fonts (Alata, Lora, Roboto) | <https://fonts.google.com> | SIL Open Font License | 테마 `head.html`에서 불러옴 |
| 빌드 스크립트 | 수업 제공 `prepare_github_pages.py` / `.github/pages_build.py` | 수업 자료 | `.github/` |
| Hugo 예제 사이트 라이선스 | 테마 ZIP의 `exampleSite/` (Hugo 프로젝트) | Apache License 2.0 — 원문 [`site/LICENSE`](site/LICENSE), [`exampleSite/LICENSE`](exampleSite/LICENSE) 유지 | `site/LICENSE` |

사이트 하단의 "Made with ❤ and Hugo Profile" 테마 출처 표시는 그대로 유지합니다.

### 콘텐츠·이미지 구분

| 파일 | 구분 | 설명 |
| --- | --- | --- |
| `site/content/**/*.md`, `site/hugo.yaml`의 소개 글 | **본인 작성 + AI 도움** | 본인이 제공한 사실을 바탕으로 AI(Claude Code)가 문장 초안·영어 번역을 작성하고 본인이 확인·수정 (상세: [`AI_LOG.md`](AI_LOG.md)) |
| `site/static/images/profile.svg` | **AI 생성** | Claude Code가 SVG 코드로 직접 그린 아바타 (실제 얼굴 사진 아님) |
| `site/static/images/projects/portfolio.svg` | **AI 생성** | Claude Code가 SVG 코드로 그린 썸네일 |
| `site/static/images/projects/review-manager/*.webp` | **직접 제작** | 본인이 만든 서비스 "리뷰 매니저 AI"의 화면을 직접 캡처 |
| `site/static/images/projects/ai-agent-challenge.png` | **외부 자료** | 2026 AI Agent Challenge 모집 포스터 (주최: 네이버 커넥트재단·서울대학교 대학연대 지역인재양성 사업단). 참가 활동 소개 목적으로만 사용 |
| `site/static/fav.png` | **AI 생성** | 탭 아이콘·상단 메뉴 로고. Claude Code가 Python(Pillow)과 Windows 기본 글꼴(맑은 고딕)로 그림 — 생성 스크립트 [`tools/make_favicon.py`](tools/make_favicon.py). 테마 원본 아이콘은 `site/themes/template/static/fav.png`에 그대로 있음 |

# site/ — 실제 사이트 폴더

이 폴더가 Hugo가 빌드하는 실제 사이트입니다. 설치·빌드·배포 방법은 저장소 루트의 [README.md](../README.md)를 보세요.

| 경로 | 내용 |
| --- | --- |
| `hugo.yaml` | 사이트 설정, 첫 화면·자기소개·대표 활동 등 소개 내용 (한국어 `params`, 영어 `languages.en.params`) |
| `pages.json` | 배포용 baseURL 등 (수업 제공 스크립트가 생성) |
| `content/ko/`, `content/en/` | 언어별 활동 글 |
| `i18n/` | 화면 문구 번역 (테마에 없는 문구만) |
| `layouts/` | 테마 템플릿 덮어쓰기 — 접근성·링크 개선 |
| `static/` | 이미지, 추가 CSS(`css/custom.css`), 아이콘 |
| `themes/template/` | Hugo Profile 테마 원본 (MIT) |

> 이 폴더의 `LICENSE`(Apache 2.0)는 테마 ZIP의 `exampleSite/`에서 함께 복사된 Hugo 프로젝트 라이선스이며, 원본 그대로 유지합니다.
> 이전에 이 자리에 있던 Hugo 프로젝트 README 원문은 `../exampleSite/README.md`에 그대로 남아 있습니다.

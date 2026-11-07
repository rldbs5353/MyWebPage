"""빌드 결과(public/)의 내부 링크·이미지·CSS·JS 경로를 검사한다.

검사 내용
  - 모든 HTML의 href/src 내부 주소가 실제 파일로 연결되는가 (깨진 링크·이미지)
  - 내부 주소가 배포 하위 경로(/MyWebPage/)로 시작하는가 (도메인 루트로 새지 않는가)
  - localhost, 127.0.0.1, file:, 개인 PC 경로(C:\\) 가 남아 있지 않은가
  - 테마 예시 문구(가상 인물·예시 링크 등)가 남아 있지 않은가

사용법 (저장소 루트에서, 먼저 `python .github/pages_build.py --build` 실행)
    python tools/check_links.py            # public/ 검사
    python tools/check_links.py 다른폴더

문제가 하나라도 있으면 종료 코드 1을 돌려준다 (GitHub Actions에서 배포 중단용).
"""
import html
import json
import re
import sys
import urllib.parse
from pathlib import Path

for stream in (sys.stdout, sys.stderr):  # Windows 콘솔에서도 한글이 깨지지 않게
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8", errors="backslashreplace")

ROOT = Path(__file__).resolve().parent.parent
public = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "public"
base_url = json.loads((ROOT / ".github-pages.json").read_text(encoding="utf-8"))["baseURL"]
parts = urllib.parse.urlsplit(base_url)
host = f"{parts.scheme}://{parts.netloc}"
prefix = parts.path.rstrip("/")  # 예: /MyWebPage

SAMPLE_TEXT = re.compile(r"Isabella|gurusabarisha|example\.com|Lorem ipsum|Facebook Hackathon", re.I)
PRIVATE_REF = re.compile(r"localhost|127\.0\.0\.1|^file:|[A-Za-z]:\\", re.I)
ATTR = re.compile(r"""(?:href|src)\s*=\s*("([^"]*)"|'([^']*)'|([^\s>]+))""")

if not (public / "index.html").is_file():
    sys.exit(f"{public}/index.html 이 없습니다. 먼저 빌드하세요: python .github/pages_build.py --build")

problems = []
pages = sorted(public.rglob("*.html"))
for page in pages:
    rel_page = page.relative_to(public).as_posix()
    text = page.read_text(encoding="utf-8")
    for m in SAMPLE_TEXT.finditer(text):
        problems.append((rel_page, "테마 예시 문구", m[0]))
    for m in ATTR.finditer(text):
        url = html.unescape(m[2] or m[3] or m[4] or "")
        if PRIVATE_REF.search(url):
            problems.append((rel_page, "개인 PC/로컬 주소", url))
            continue
        if url.startswith(host):
            url = url[len(host):]
        if not url or url.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
            continue
        if url.startswith(("http://", "https://", "//")):
            continue  # 외부 링크는 별도 확인
        path = urllib.parse.unquote(urllib.parse.urlsplit(url).path)
        if not path.startswith("/"):
            path = "/" + (Path(rel_page).parent / path).as_posix()
        if prefix and not (path == prefix or path.startswith(prefix + "/")):
            problems.append((rel_page, "하위 경로 누락", url))
            continue
        target = public / path[len(prefix):].lstrip("/")
        if not (target.is_file() or (target / "index.html").is_file()):
            problems.append((rel_page, "파일 없음", url))

for page, kind, detail in sorted(set(problems)):
    print(f"[{kind}] {page}: {detail}")
print(f"검사한 HTML {len(pages)}개, 문제 {len(set(problems))}건")
sys.exit(1 if problems else 0)

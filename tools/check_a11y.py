"""빌드 결과(public/)의 기본 접근성 항목을 검사한다.

검사 내용 (채점 기준 번호)
  - P48  <html lang> 이 있고 언어 폴더와 맞는가 (/en/ → en, 그 외 → ko)
  - P47  실제 페이지마다 <h1> 이 정확히 1개인가
  - P45  모든 <img> 에 alt 속성이 있는가 (장식 이미지는 alt="" 허용)
  - P46  아이콘만 있는 링크·버튼에 aria-label / title 등 이름이 있는가
  - P29  의미 없는 href="#" 링크가 없는가

사용법 (저장소 루트에서, 먼저 빌드)
    python tools/check_a11y.py           # public/ 검사
문제가 있으면 종료 코드 1.
"""
import re
import sys
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8", errors="backslashreplace")

ROOT = Path(__file__).resolve().parent.parent
public = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "public"
if not (public / "index.html").is_file():
    sys.exit(f"{public}/index.html 이 없습니다. 먼저 빌드하세요: python .github/pages_build.py --build")

TAG_TEXT = re.compile(r"<[^>]+>")
NAMED = re.compile(r"\b(aria-label|aria-labelledby|title)\s*=", re.I)

problems = []
pages = 0
for page in sorted(public.rglob("*.html")):
    text = page.read_text(encoding="utf-8")
    rel = page.relative_to(public).as_posix()
    if re.search(r'http-equiv=["\']?refresh', text, re.I):
        continue  # Hugo가 만드는 자동 이동(alias) 페이지는 제외
    pages += 1

    m = re.search(r"<html\b[^>]*\blang=[\"']?([\w-]+)", text, re.I)
    expected = "en" if rel.startswith("en/") else "ko"
    if not m:
        problems.append((rel, "P48 lang 없음", ""))
    elif m[1].lower().split("-")[0] != expected:
        problems.append((rel, "P48 lang 불일치", f"{m[1]} (예상 {expected})"))

    h1 = len(re.findall(r"<h1\b", text, re.I))
    if h1 != 1:
        problems.append((rel, "P47 h1 개수", str(h1)))

    for img in re.findall(r"<img\b[^>]*>", text, re.I):
        if not re.search(r"\balt(\s*=|[\s>/])", img, re.I):
            problems.append((rel, "P45 alt 없음", img[:100]))

    for a in re.finditer(r"<(a|button)\b([^>]*)>(.*?)</\1>", text, re.I | re.S):
        attrs, inner = a[2], a[3]
        visible = TAG_TEXT.sub("", re.sub(r"<[^>]*aria-hidden=[\"']?true[^>]*>.*?</[^>]+>", "", inner, flags=re.S)).strip()
        img_alt = re.search(r"<img\b[^>]*\balt=[\"']([^\"']+)", inner, re.I)
        if not visible and not NAMED.search(attrs) and not img_alt:
            problems.append((rel, "P46 이름 없는 아이콘 조작", attrs.strip()[:100]))
        if a[1].lower() == "a" and re.search(r"\bhref=[\"']?#[\"'\s>]", attrs + ">"):
            problems.append((rel, "P29 href=\"#\"", attrs.strip()[:100]))

for rel, kind, detail in sorted(set(problems)):
    print(f"[{kind}] {rel}: {detail}")
print(f"검사한 페이지 {pages}개, 문제 {len(set(problems))}건")
sys.exit(1 if problems else 0)

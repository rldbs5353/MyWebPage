"""사이트 아이콘(site/static/fav.png) 생성 스크립트.

남색 둥근 사각형(프로필 아바타 후드 색) 위에 흰색 '엄'과 작은 </> 표시를 그린다.
필요: Python 3, Pillow (pip install pillow), Windows 기본 글꼴(맑은 고딕 굵게, Consolas 굵게)

사용법 (저장소 루트에서):
    python tools/make_favicon.py            # site/static/fav.png 덮어쓰기
    python tools/make_favicon.py out.png    # 다른 경로로 저장
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

out = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parent.parent / "site" / "static" / "fav.png")
S = 256
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
d.rounded_rectangle([0, 0, S - 1, S - 1], radius=56, fill=(30, 58, 138, 255))  # #1e3a8a
d.rounded_rectangle([10, 10, S - 11, S - 11], radius=48, outline=(96, 165, 250, 255), width=6)  # #60a5fa

font = ImageFont.truetype(r"C:\Windows\Fonts\malgunbd.ttf", 150)
text = "엄"
box = d.textbbox((0, 0), text, font=font)
w, h = box[2] - box[0], box[3] - box[1]
d.text(((S - w) / 2 - box[0], (S - h) / 2 - box[1] - 14), text, font=font, fill=(255, 255, 255, 255))

small = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 40)
code = "</>"
b2 = d.textbbox((0, 0), code, font=small)
d.text(((S - (b2[2] - b2[0])) / 2 - b2[0], S - 62), code, font=small, fill=(147, 197, 253, 255))

img.save(out, optimize=True)
print("saved", out, img.size)

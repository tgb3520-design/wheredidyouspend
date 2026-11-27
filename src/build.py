# src/app.html 의 /*TABLE*/ 자리에 간이세액표를 넣어 public/index.html 을 만든다.
from pathlib import Path
here = Path(__file__).parent
html = (here / "app.html").read_text(encoding="utf-8")
table = (here / "tax-table.js").read_text(encoding="utf-8")
(here.parent / "public" / "index.html").write_text(html.replace("/*TABLE*/", table), encoding="utf-8")

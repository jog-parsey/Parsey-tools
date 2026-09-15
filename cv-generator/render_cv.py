#!/usr/bin/env python3
"""Render a Parsey-brand CV PDF from structured JSON data.

Usage: python3 render_cv.py data.json output.pdf
"""
import sys
import json
import base64
from pathlib import Path
from jinja2 import Template
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent

def b64(path):
    return base64.b64encode((HERE / path).read_bytes()).decode()

def main():
    data_path, out_path = sys.argv[1], sys.argv[2]
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))

    data.setdefault("total_pages", 3)
    data.setdefault("navn_footer", data.get("navn", "").upper())
    data.setdefault("photo_b64", None)
    if data.get("photo_path"):
        data["photo_b64"] = base64.b64encode(Path(data["photo_path"]).read_bytes()).decode()

    data.setdefault("sikkerhedsgodkendelse", None)
    data.setdefault("certificeringer", [])
    cert_lines = list(data.get("kurser", []))
    for c in data["certificeringer"]:
        line = c.get("navn", "")
        detail = ", ".join(x for x in [c.get("udsteder"), str(c.get("aar") or "")] if x)
        if detail:
            line += f" ({detail})"
        if c.get("udloeber"):
            line += f" — gyldig til {c['udloeber']}"
        cert_lines.append(line)
    data["cert_lines"] = cert_lines

    tpl = Template((HERE / "template.html.j2").read_text(encoding="utf-8"))
    html = tpl.render(
        sg_bold=b64("fonts/SpaceGrotesk-Bold.woff2"),
        sg_medium=b64("fonts/SpaceGrotesk-Medium.woff2"),
        inter_reg=b64("fonts/Inter-Regular.woff2"),
        inter_semi=b64("fonts/Inter-SemiBold.woff2"),
        **data,
    )

    html_path = Path(out_path).with_suffix(".html")
    html_path.write_text(html, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path.resolve()}")
        page.wait_for_timeout(200)
        page.pdf(
            path=out_path,
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        browser.close()
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()

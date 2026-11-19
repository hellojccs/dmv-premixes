"""Genera prototipo/index.html insertando el logo autorizado (brand/logos) en la plantilla."""
import re, pathlib, base64
root = pathlib.Path(__file__).resolve().parents[2]
svg = (root / "brand/logos/dmv-logo-primary-black.svg").read_text()
paths = re.findall(r'<path class="cls-1" d="([^"]+)"', svg)
mark = "".join(f'<path d="{d}"/>' for d in paths[:3])
word = "".join(f'<path d="{d}"/>' for d in paths[3:])
tpl = (root / "prototipo/src/index.template.html").read_text()
font = base64.b64encode((root / "brand/fonts/Rinter-Regular.woff2").read_bytes()).decode()
logos = sorted((root / "brand/clientes-ejemplo").glob("*.svg"))
def items(hidden):
    out = []
    for f in logos:
        svg = re.sub(r'\s(xmlns|role|aria-label)="[^"]*"', "", f.read_text().strip())
        svg = svg.replace("<svg", '<svg aria-hidden="true"' if hidden else f'<svg role="img" aria-label="{f.stem.replace("-", " ").title()}"', 1)
        out.append(f'<div class="marquee-item">{svg}</div>')
    return "".join(out)
out = (tpl.replace("{{CLIENT_LOGOS}}", items(False)).replace("{{CLIENT_LOGOS_COPY}}", items(True))
          .replace("{{REVEAL}}", (root / "elementor/fragmentos/color-swipe-reveal.html").read_text())
          .replace("{{STACK}}", (root / "elementor/fragmentos/tarjetas-apiladas.html").read_text())
          .replace("{{MARK}}", mark).replace("{{WORD}}", word)
          .replace("{{RINTER_WOFF2}}", "data:font/woff2;base64," + font))
(root / "prototipo/index.html").write_text(out)
print("OK prototipo/index.html", len(out), "bytes")

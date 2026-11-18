"""Genera prototipo/index.html insertando el logo autorizado (brand/logos) en la plantilla."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
svg = (root / "brand/logos/dmv-logo-primary-black.svg").read_text()
paths = re.findall(r'<path class="cls-1" d="([^"]+)"', svg)
mark = "".join(f'<path d="{d}"/>' for d in paths[:3])
word = "".join(f'<path d="{d}"/>' for d in paths[3:])
tpl = (root / "prototipo/src/index.template.html").read_text()
out = tpl.replace("{{MARK}}", mark).replace("{{WORD}}", word)
(root / "prototipo/index.html").write_text(out)
print("OK prototipo/index.html", len(out), "bytes")

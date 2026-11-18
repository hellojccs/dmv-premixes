"""Genera las plantillas de Elementor (JSON importables) en elementor/plantillas/.

Uso:  python3 elementor/src/generar.py
"""
import json, re, hashlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "elementor/plantillas"

# Paleta autorizada
RB, SG, CS, TG, CB, WS = "#195DE4", "#E9E6DF", "#8798B2", "#5A5154", "#1C1B17", "#F6F7F2"
WA_GREEN = "#25D366"          # excepción aprobada: botón de WhatsApp
WHATSAPP = "https://wa.me/525543577104"
LOGO_WHITE = "https://dmvpremixes.com/wp-content/uploads/Asset-6DMV_LOGO_PRIMARY_WHITE-1024x203.png"

_n = 0
def rid(seed):
    """IDs estables (mismo resultado en cada generación)."""
    global _n; _n += 1
    return hashlib.md5(f"{seed}-{_n}".encode()).hexdigest()[:7]

def px(v, u="px"): return {"unit": u, "size": v, "sizes": []}
def box(t, r, b, l, u="px"):
    return {"unit": u, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}
def radius(v): return {"unit": "px", "top": str(v), "right": str(v), "bottom": str(v), "left": str(v), "isLinked": True}
def typo(prefix, fam, size, size_m=None, lh=None, ls=None):
    d = {f"{prefix}_typography": "custom", f"{prefix}_font_family": fam,
         f"{prefix}_font_weight": "400", f"{prefix}_font_size": px(size)}
    if size_m: d[f"{prefix}_font_size_mobile"] = px(size_m)
    if lh: d[f"{prefix}_line_height"] = px(lh, "em")
    if ls is not None: d[f"{prefix}_letter_spacing"] = px(ls)
    return d

def widget(kind, settings): return {"id": rid(kind), "elType": "widget", "widgetType": kind, "settings": settings, "elements": [], "isInner": False}
def container(settings, elements, inner=False):
    return {"id": rid("con"), "elType": "container", "isInner": inner, "settings": settings, "elements": elements}

def button(text, url, *, outline_white=False, size=15, pad=(14, 40), extra=None):
    s = {"text": text, "link": {"url": url, "is_external": "", "nofollow": "", "custom_attributes": ""},
         "selected_icon": {"value": "fas fa-arrow-right", "library": "fa-solid"}, "icon_align": "right", "icon_indent": px(12),
         "button_text_color": WS, "background_color": RB,
         "button_background_background": "classic", "button_background_color": RB,
         "border_radius": radius(999), "text_padding": box(pad[0], pad[1], pad[0], pad[1])}
    if outline_white:
        s.update({"hover_color": RB, "button_background_hover_background": "classic", "button_background_hover_color": WS,
                  "border_border": "solid", "border_width": radius(1), "border_color": WS})
    else:
        s.update({"hover_color": WS, "button_background_hover_background": "classic", "button_background_hover_color": "#1450C6"})
    s.update(typo("typography", "Rinter", size))
    if extra: s.update(extra)
    return widget("button", s)

def save(name, title, kind, content):
    OUT.mkdir(parents=True, exist_ok=True)
    tpl = {"content": content, "page_settings": {}, "version": "0.4", "title": title, "type": kind}
    (OUT / name).write_text(json.dumps(tpl, ensure_ascii=False, indent=2))
    print("OK", name)

# ------------------------------------------------------------------ HERO
def hero():
    return [container({
        "_title": "Hero",
        "content_width": "boxed", "boxed_width": px(1120),
        "flex_direction": "column", "flex_justify_content": "center", "flex_align_items": "center",
        "flex_gap": {"column": "0", "row": "0", "isLinked": True, "unit": "px", "size": 0},
        "padding": box(170, 24, 80, 24), "padding_mobile": box(130, 16, 64, 16),
        "background_background": "classic", "background_color": RB,
        "background_overlay_background": "gradient",
        "background_overlay_color": "rgba(28,27,23,0.28)", "background_overlay_color_stop": px(0, "%"),
        "background_overlay_color_b": "rgba(246,247,242,0.24)", "background_overlay_color_b_stop": px(100, "%"),
        "background_overlay_gradient_type": "linear", "background_overlay_gradient_angle": px(180, "deg"),
        "background_overlay_opacity": px(1),
    }, [
        widget("image", {
            "image": {"url": LOGO_WHITE, "id": "", "alt": "DMV Premixes", "source": "library", "size": ""},
            "image_size": "full", "align": "center", "width": px(500), "width_mobile": px(80, "%"),
            "_margin": box(0, 0, 48, 0)}),
        widget("heading", {"title": "Precisión en cada formulación", "header_size": "h1", "align": "center",
                           "title_color": WS, **typo("typography", "Rinter", 64, 36, 1.12, -1)}),
        widget("text-editor", {
            "editor": "<p>DMV Premixes es una marca especializada en el desarrollo y suministro de premezclas nutricionales personalizadas para las industrias de alimentos, bebidas y nutrición animal.</p>",
            "align": "center", "text_color": WS,
            "_element_width": "initial", "_element_custom_width": px(800), "_element_custom_width_mobile": px(100, "%"),
            "_margin": box(22, 0, 40, 0), **typo("typography", "Archivo", 18, 16, 1.6)}),
        container({
            "_title": "Botones", "content_width": "full", "width": px(100, "%"),
            "flex_direction": "row", "flex_direction_mobile": "column",
            "flex_justify_content": "center", "flex_align_items": "center", "flex_align_items_mobile": "stretch",
            "flex_gap": {"column": "20", "row": "14", "isLinked": False, "unit": "px", "size": 20},
            "padding": box(0, 0, 0, 0)},
            [button("Ver Soluciones", "#soluciones", outline_white=True, extra={"align_mobile": "justify"}),
             button("Consulta una asesoría", "#contacto", outline_white=True, extra={"align_mobile": "justify"})],
            inner=True),
    ])]

# ------------------------------------------------------------------ HEADER
def mark_svg():
    svg = (ROOT / "brand/logos/dmv-logo-primary-white.svg").read_text()
    paths = re.findall(r'<path class="cls-1" d="([^"]+)"', svg)[:3]   # solo el símbolo
    inner = "".join(f'<path d="{d}"/>' for d in paths)
    return ('<a href="/" class="dmv-mark" aria-label="DMV Premixes — Inicio">'
            f'<svg viewBox="0 0 248.1 207.64" fill="{WS}" aria-hidden="true">{inner}</svg></a>')

HEADER_CSS_OUTER = """/* Header flotante sobre el contenido */
selector{position:fixed;top:0;left:0;right:0;z-index:999;pointer-events:none;}
selector > .e-con-inner, selector > .e-con{pointer-events:auto;}
body.admin-bar selector{top:32px;}
@media (max-width:782px){body.admin-bar selector{top:46px;}}"""

HEADER_CSS_PILL = """/* Efecto vidrio */
selector{pointer-events:auto;-webkit-backdrop-filter:blur(18px) saturate(1.4);backdrop-filter:blur(18px) saturate(1.4);}
/* Símbolo del logo en círculo azul */
selector .dmv-mark{width:38px;height:38px;border-radius:50%;background:#195DE4;display:grid;place-items:center;}
selector .dmv-mark svg{width:20px;height:auto;}"""

def header():
    return [container({
        "_title": "Header (fijo)",
        "content_width": "full",
        "flex_direction": "row", "flex_justify_content": "center", "flex_align_items": "center",
        "padding": box(16, 24, 0, 24), "padding_mobile": box(16, 16, 0, 16),
        "custom_css": HEADER_CSS_OUTER,
    }, [container({
        "_title": "Barra (vidrio)",
        "content_width": "full", "width": px(680), "width_mobile": px(100, "%"),
        "flex_direction": "row", "flex_justify_content": "space-between", "flex_align_items": "center",
        "flex_wrap": "nowrap",
        "flex_gap": {"column": "8", "row": "8", "isLinked": True, "unit": "px", "size": 8},
        "padding": box(8, 8, 8, 10),
        "background_background": "classic", "background_color": "rgba(255,255,255,0.55)",
        "border_border": "solid", "border_width": radius(1), "border_color": "rgba(255,255,255,0.75)",
        "border_radius": radius(999),
        "box_shadow_box_shadow_type": "yes",
        "box_shadow_box_shadow": {"horizontal": 0, "vertical": 8, "blur": 30, "spread": 0, "color": "rgba(25,93,228,0.12)"},
        "custom_css": HEADER_CSS_PILL,
    }, [
        widget("html", {"_title": "Símbolo DMV", "html": mark_svg()}),
        widget("nav-menu", {
            "_title": "Menú",
            "menu": "",                       # elegir tu menú en el panel
            "layout": "horizontal", "align_items": "center", "pointer": "none",
            "submenu_icon": {"value": "fas fa-chevron-down", "library": "fa-solid"},
            "dropdown": "mobile", "toggle": "burger", "toggle_align": "right", "full_width": "yes",
            "_flex_size": "grow",
            **typo("menu_typography", "Archivo", 14),
            "color_menu_item": CB, "color_menu_item_hover": RB, "color_menu_item_active": RB,
            "padding_horizontal_menu_item": px(12), "padding_vertical_menu_item": px(8),
            "menu_space_between": px(4),
            "color_dropdown_item": CB, "background_color_dropdown_item": "#FFFFFF",
            "color_dropdown_item_hover": RB, "background_color_dropdown_item_hover": WS,
            **typo("dropdown_typography", "Archivo", 14),
            "dropdown_border_radius": radius(12),
            "toggle_color": CB, "toggle_background_color": "rgba(0,0,0,0)",
            "toggle_border_width": px(1), "toggle_border_radius": px(999),
        }),
        widget("icon", {
            "_title": "WhatsApp",
            "selected_icon": {"value": "fab fa-whatsapp", "library": "fa-brands"},
            "view": "stacked", "shape": "circle",
            "primary_color": WA_GREEN, "secondary_color": "#FFFFFF",
            "hover_primary_color": TG, "hover_secondary_color": "#FFFFFF",
            "size": px(20), "icon_padding": px(10),
            "link": {"url": WHATSAPP, "is_external": "on", "nofollow": "", "custom_attributes": ""},
        }),
        button("Contáctanos", "/contactanos/", size=14, pad=(11, 18), extra={"hide_mobile": "hidden-mobile"}),
    ], inner=True)])]

if __name__ == "__main__":
    save("01-hero-prueba.json", "DMV - Hero (prueba)", "container", hero())
    save("02-header.json", "DMV - Header", "header", header())

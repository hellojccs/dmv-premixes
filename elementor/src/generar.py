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

RINTER_SHIFT = 0.143   # em: Rinter se ve 0.143em arriba del centro; se compensa con padding (sin tocar la fuente)

def button(text, url, *, outline_white=False, size=15, pad=(14, 40), extra=None):
    d = round(size * RINTER_SHIFT)
    s = {"text": text, "link": {"url": url, "is_external": "", "nofollow": "", "custom_attributes": ""},
         "button_text_color": WS, "background_color": RB,
         "button_background_background": "classic", "button_background_color": RB,
         "border_radius": radius(999), "text_padding": box(pad[0] + d, pad[1], pad[0] - d, pad[1])}
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
def brand_html():
    svg = (ROOT / "brand/logos/dmv-logo-primary-white.svg").read_text()
    paths = re.findall(r'<path class="cls-1" d="([^"]+)"', svg)
    full = "".join(f'<path d="{d}"/>' for d in paths)
    mark = "".join(f'<path d="{d}"/>' for d in paths[:3])
    return (
        '<a href="/" class="dmv-brand" aria-label="DMV Premixes — Inicio">'
        f'<svg class="dmv-logo-full" viewBox="0 0 1049.08 207.64" fill="{WS}" aria-hidden="true">{full}</svg>'
        f'<span class="dmv-mark"><svg viewBox="0 0 248.1 207.64" fill="{WS}" aria-hidden="true">{mark}</svg></span>'
        '</a>\n'
        '<script>(function(){function u(){document.body.classList.toggle("dmv-scrolled",window.scrollY>40)}'
        'window.addEventListener("scroll",u,{passive:true});u();})();</script>')

HEADER_CSS_OUTER = """/* Header flotante: dos barras (izquierda logo + menú · derecha acciones) */
selector{position:fixed;top:0;left:0;right:0;z-index:999;pointer-events:none;}
body.admin-bar selector{top:32px;}
@media (max-width:782px){body.admin-bar selector{top:46px;}}"""

GLASS_CSS = """/* Vidrio claro arriba; vidrio Carbon Black al hacer scroll */
selector{pointer-events:auto;--width:auto;width:auto;flex:0 0 auto;-webkit-backdrop-filter:blur(18px) saturate(1.4);backdrop-filter:blur(18px) saturate(1.4);transition:background-color .3s,border-color .3s;}
body.dmv-scrolled selector{background-color:rgba(28,27,23,.84) !important;border-color:rgba(246,247,242,.12) !important;}"""

LEFT_CSS = GLASS_CSS + """

/* Logo completo arriba, solo el símbolo al hacer scroll */
selector .dmv-brand{position:relative;display:block;height:40px;width:158px;transition:width .35s ease;}
selector .dmv-logo-full{position:absolute;left:12px;top:50%;width:142px;height:auto;transform:translateY(-50%);transition:opacity .25s,transform .35s;}
selector .dmv-mark{position:absolute;left:0;top:0;width:40px;height:40px;border-radius:50%;background:#195DE4;display:grid;place-items:center;opacity:0;transform:scale(.6);transition:opacity .25s,transform .35s;}
selector .dmv-mark svg{width:20px;height:auto;}
body.dmv-scrolled selector .dmv-brand{width:40px;}
body.dmv-scrolled selector .dmv-logo-full{opacity:0;transform:translateY(-50%) scale(.92);}
body.dmv-scrolled selector .dmv-mark{opacity:1;transform:none;}
@media (max-width:767px){selector .dmv-brand{width:140px;}selector .dmv-logo-full{width:124px;}}

/* Menú: texto blanco; hover con fondo Royal Blue al 50% */
selector .elementor-nav-menu--main .elementor-item{height:40px;display:flex;align-items:center;padding-top:0;padding-bottom:0;border-radius:12px;transition:background-color .2s;}
selector .elementor-nav-menu--main .elementor-item:hover,
selector .elementor-nav-menu--main .elementor-item:focus,
selector .elementor-nav-menu--main .elementor-item.highlighted{background-color:rgba(25,93,228,.5);color:#F6F7F2;}
selector .elementor-nav-menu--dropdown{min-width:220px;border-radius:12px;overflow:hidden;box-shadow:0 20px 48px rgba(28,27,23,.12);}
selector .elementor-nav-menu--dropdown a{white-space:nowrap;}

/* Botón ⋮ / hamburguesa: círculo perfecto de 40px */
selector .elementor-menu-toggle{width:40px;height:40px;padding:0;margin:0;border:0;border-radius:50%;background-color:rgba(246,247,242,.12);align-items:center;justify-content:center;box-sizing:border-box;}
/* Solo se muestra en celular, o en escritorio al hacer scroll (regla de abajo); arriba en escritorio queda oculto */
@media (min-width:768px){selector .elementor-menu-toggle{display:none;}}
@media (max-width:767px){selector .elementor-menu-toggle{display:flex;}}
selector .elementor-menu-toggle:hover,selector .elementor-menu-toggle.elementor-active{background-color:rgba(25,93,228,.5);}
selector .elementor-menu-toggle svg{width:20px;height:20px;}
selector .elementor-menu-toggle i{font-size:20px;}

/* Panel del menú: debajo de la barra, alineado a su borde izquierdo */
selector .elementor-widget-nav-menu,selector .elementor-widget-nav-menu .elementor-widget-container{position:static;}
selector .elementor-nav-menu__container.elementor-nav-menu--dropdown{position:absolute;top:calc(100% + 8px);left:0;min-width:280px;z-index:20;}
@media (max-width:767px){selector .elementor-nav-menu__container.elementor-nav-menu--dropdown{width:calc(100vw - 32px);}}

/* Al hacer scroll (escritorio): se ocultan los enlaces y aparece el botón ⋮ (referencia Butter) */
@media (min-width:768px){
  body.dmv-scrolled selector .elementor-nav-menu--main{display:none;}
  body.dmv-scrolled selector .elementor-menu-toggle{display:flex;}
  body.dmv-scrolled selector .elementor-nav-menu--dropdown{display:block;}
  body.dmv-scrolled selector .elementor-menu-toggle:not(.elementor-active) .elementor-menu-toggle__icon--open{display:none;}
  body.dmv-scrolled selector .elementor-menu-toggle:not(.elementor-active)::before{content:"";display:block;width:20px;height:20px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23F6F7F2'%3E%3Ccircle cx='12' cy='5' r='1.8'/%3E%3Ccircle cx='12' cy='12' r='1.8'/%3E%3Ccircle cx='12' cy='19' r='1.8'/%3E%3C/svg%3E") center/contain no-repeat;}
}"""

RIGHT_CSS = GLASS_CSS + """

/* Botón Contáctanos: borde blanco arriba, sin borde al hacer scroll */
selector .elementor-icon-wrapper{display:flex;line-height:0;}
selector .elementor-icon{width:40px;height:40px;padding:0;display:flex;align-items:center;justify-content:center;font-size:20px;}
selector .elementor-icon svg{width:20px;height:20px;}
/* Rinter: +2px arriba / -2px abajo para centrar el texto */
selector .elementor-button{height:40px;padding:2px 22px 0;display:inline-flex;align-items:center;box-sizing:border-box;border:1px solid #F6F7F2;}
body.dmv-scrolled selector .elementor-button{border-color:transparent;}"""

def glass(title, pad, css, elements):
    return container({
        "_title": title,
        "content_width": "full",
        "flex_direction": "row", "flex_justify_content": "flex-start", "flex_align_items": "center",
        "flex_wrap": "nowrap",
        "flex_gap": {"column": "12", "row": "8", "isLinked": False, "unit": "px", "size": 12},
        "padding": pad,
        "background_background": "classic", "background_color": "rgba(246,247,242,0.14)",
        "border_border": "solid", "border_width": radius(1), "border_color": "rgba(246,247,242,0.35)",
        "border_radius": radius(999),
        "box_shadow_box_shadow_type": "yes",
        "box_shadow_box_shadow": {"horizontal": 0, "vertical": 8, "blur": 30, "spread": 0, "color": "rgba(28,27,23,0.10)"},
        "custom_css": css,
    }, elements, inner=True)

def header():
    left = glass("Barra izquierda: logo + menú", box(6, 6, 6, 6), LEFT_CSS, [
        widget("html", {"_title": "Logo DMV (completo / símbolo)", "html": brand_html()}),
        widget("nav-menu", {
            "_title": "Menú",
            "menu": "",                       # elegir tu menú en el panel
            "layout": "horizontal", "align_items": "center", "pointer": "none",
            "submenu_icon": {"value": "fas fa-chevron-down", "library": "fa-solid"},
            "dropdown": "mobile", "toggle": "burger", "toggle_align": "right", "full_width": "",
            **typo("menu_typography", "Archivo", 14),
            "color_menu_item": WS, "color_menu_item_hover": WS, "color_menu_item_active": WS,
            "padding_horizontal_menu_item": px(14), "padding_vertical_menu_item": px(0),
            "menu_space_between": px(2),
            "color_dropdown_item": CB, "background_color_dropdown_item": "#FFFFFF",
            "color_dropdown_item_hover": CB, "background_color_dropdown_item_hover": "rgba(25,93,228,0.12)",
            **typo("dropdown_typography", "Archivo", 14),
            "toggle_color": WS, "toggle_color_hover": WS,
            "toggle_background_color": "rgba(246,247,242,0.12)", "toggle_background_color_hover": "rgba(25,93,228,0.5)",
            "toggle_border_width": px(0), "toggle_border_radius": px(999), "toggle_size": px(20),
        }),
    ])
    right = glass("Barra derecha: WhatsApp + Contáctanos", box(6, 6, 6, 6), RIGHT_CSS, [
        widget("icon", {
            "_title": "WhatsApp",
            "selected_icon": {"value": "fab fa-whatsapp", "library": "fa-brands"},
            "view": "stacked", "shape": "circle",
            "primary_color": WA_GREEN, "secondary_color": "#FFFFFF",
            "hover_primary_color": TG, "hover_secondary_color": "#FFFFFF",
            "size": px(20), "icon_padding": px(10),
            "link": {"url": WHATSAPP, "is_external": "on", "nofollow": "", "custom_attributes": ""},
        }),
        button("Contáctanos", "/contactanos/", size=14, pad=(11, 20), extra={"hide_mobile": "hidden-mobile"}),
    ])
    return [container({
        "_title": "Header (fijo)",
        "content_width": "boxed", "boxed_width": px(1120),
        "flex_direction": "row", "flex_justify_content": "space-between", "flex_align_items": "center",
        "flex_wrap": "nowrap",
        "flex_gap": {"column": "12", "row": "12", "isLinked": True, "unit": "px", "size": 12},
        "padding": box(16, 24, 0, 24), "padding_mobile": box(16, 16, 0, 16),
        "custom_css": HEADER_CSS_OUTER,
    }, [left, right])]

if __name__ == "__main__":
    save("01-hero-prueba.json", "DMV - Hero (prueba)", "container", hero())
    save("02-header.json", "DMV - Header", "header", header())

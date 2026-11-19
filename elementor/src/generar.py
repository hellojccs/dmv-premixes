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

# Botones: Archivo 14 / 400, igual que el menú del header (decisión del cliente).
# (Si algún día vuelven a Rinter: compensar 0.143em con +2px arriba / -2px abajo.)

def button(text, url, *, outline_white=False, size=15, pad=(14, 40), extra=None):
    d = 0
    s = {"text": text, "link": {"url": url, "is_external": "", "nofollow": "", "custom_attributes": ""},
         "button_text_color": WS, "background_color": RB,
         "button_background_background": "classic", "button_background_color": RB,
         "border_radius": radius(999), "text_padding": box(pad[0] + d, pad[1], pad[0] - d, pad[1])}
    if outline_white:
        s.update({"hover_color": RB, "button_background_hover_background": "classic", "button_background_hover_color": WS,
                  "border_border": "solid", "border_width": radius(1), "border_color": WS})
    else:
        s.update({"hover_color": WS, "button_background_hover_background": "classic", "button_background_hover_color": "#1450C6"})
    s.update(typo("typography", "Archivo", 14))
    if extra: s.update(extra)
    return widget("button", s)

def save(name, title, kind, content):
    OUT.mkdir(parents=True, exist_ok=True)
    tpl = {"content": content, "page_settings": {}, "version": "0.4", "title": title, "type": kind}
    (OUT / name).write_text(json.dumps(tpl, ensure_ascii=False, indent=2))
    print("OK", name)

# ------------------------------------------------------------------ HERO
MARQUEE_CSS = """<style>
.dmv-marquee{position:relative;width:100vw;margin:110px 0 0 calc(50% - 50vw);overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);}
.dmv-marquee-track{display:flex;width:max-content;animation:dmv-marquee 32s linear infinite;}
.dmv-marquee:hover .dmv-marquee-track{animation-play-state:paused;}
.dmv-marquee-item{flex:none;width:250px;display:flex;align-items:center;justify-content:center;color:#F6F7F2;opacity:.82;transition:opacity .2s;}
.dmv-marquee-item:hover{opacity:1;}
.dmv-marquee-item svg{height:46px;width:auto;max-width:200px;}
@keyframes dmv-marquee{to{transform:translateX(-50%);}}
@media (prefers-reduced-motion:reduce){.dmv-marquee-track{animation:none;}}
@media (max-width:767px){.dmv-marquee{margin-top:72px;}.dmv-marquee-item{width:200px;}.dmv-marquee-item svg{height:38px;}}
</style>"""

def marquee_html():
    """Franja animada con logos de clientes. Hoy: marcas FICTICIAS de ejemplo (brand/clientes-ejemplo)."""
    logos = sorted((ROOT / "brand/clientes-ejemplo").glob("*.svg"))
    def items(hidden):
        out = []
        for f in logos:
            svg = re.sub(r'\s(xmlns|role|aria-label)="[^"]*"', "", f.read_text().strip())
            label = f.stem.replace("-", " ").title()
            svg = svg.replace("<svg", '<svg aria-hidden="true"' if hidden else f'<svg role="img" aria-label="{label}"', 1)
            out.append(f'<div class="dmv-marquee-item">{svg}</div>')
        return "\n".join(out)
    return (MARQUEE_CSS + "\n<!-- Logos de clientes: marcas de EJEMPLO. Reemplazar por los logos reales. -->\n"
            '<div class="dmv-marquee" aria-label="Clientes"><div class="dmv-marquee-track">\n'
            + items(False) + "\n<!-- copia para el desplazamiento continuo -->\n" + items(True) + "\n</div></div>")

def hero():
    return [container({
        "_title": "Hero",
        "content_width": "boxed", "boxed_width": px(1120),
        "flex_direction": "column", "flex_justify_content": "center", "flex_align_items": "center",
        "flex_gap": {"column": "0", "row": "0", "isLinked": True, "unit": "px", "size": 0},
        "padding": box(170, 24, 64, 24), "padding_mobile": box(130, 16, 56, 16),
        "overflow": "hidden",
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
        widget("html", {"_title": "Franja de logos de clientes", "_element_width": "inherit", "html": marquee_html()}),
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

/* Menú: texto blanco; hover encerrado en una píldora con borde White Sand (como "Contáctanos") */
selector .elementor-nav-menu--main .elementor-item{height:40px;display:flex;align-items:center;padding-top:0;padding-bottom:0;border:1px solid transparent;border-radius:999px;transition:border-color .2s,background-color .2s;}
selector .elementor-nav-menu--main .elementor-item:hover,
selector .elementor-nav-menu--main .elementor-item:focus,
selector .elementor-nav-menu--main .elementor-item.highlighted{border-color:#F6F7F2;background-color:rgba(246,247,242,.10);color:#F6F7F2;}
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
/* Botón Contáctanos: Archivo 14, alto 40px */
selector .elementor-button{height:40px;padding:0 22px;display:inline-flex;align-items:center;box-sizing:border-box;border:1px solid #F6F7F2;}
body.dmv-scrolled selector .elementor-button{border-color:transparent;}

/* Contáctanos: mismo hover que el menú (píldora con borde White Sand y fondo blanco suave) */
selector .elementor-button{transition:border-color .2s,background-color .2s,color .2s;}
selector .elementor-button:hover,
selector .elementor-button:focus{background-color:rgba(246,247,242,.10) !important;border-color:#F6F7F2 !important;color:#F6F7F2 !important;}"""

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
        widget("icon", {
            "_title": "Carrito (tienda)",
            "selected_icon": {"value": "fas fa-shopping-cart", "library": "fa-solid"},
            "view": "stacked", "shape": "circle",
            "primary_color": CS, "secondary_color": WS,
            "hover_primary_color": TG, "hover_secondary_color": WS,
            "size": px(20), "icon_padding": px(10),
            "link": {"url": "#", "is_external": "", "nofollow": "", "custom_attributes": "aria-label|Tienda"},
            "custom_css": "selector .elementor-icon{transition:background-color .2s,box-shadow .2s;}\nselector .elementor-icon:hover{box-shadow:0 0 0 1px #F6F7F2;}",
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

# ------------------------------------------------------------------ FOOTER
def heading4(text):
    return widget("heading", {"title": text, "header_size": "h4", "title_color": WS,
                              "_margin": box(0, 0, 18, 0), **typo("typography", "Rinter", 17, None, 1.2)})

def link_list(items):
    return widget("icon-list", {
        "view": "traditional",
        "icon_list": [{"_id": rid("li"), "text": text,
                       "selected_icon": {"value": "", "library": ""},
                       "link": {"url": url, "is_external": "on" if url.startswith("http") else "", "nofollow": "", "custom_attributes": ""}}
                      for text, url in items],
        "space_between": px(10), "text_color": SG, "text_color_hover": "#FFFFFF",
        "custom_css": "selector .elementor-icon-list-text{overflow-wrap:anywhere;}",
        **typo("icon_typography", "Archivo", 14, None, 1.5),
    })

FORM_CSS = """selector .elementor-field-group .elementor-field{height:46px;padding:0 18px;border-radius:999px;}
selector .elementor-field::placeholder{color:#8798B2;opacity:1;}
selector .elementor-field:focus{border-color:#F6F7F2 !important;box-shadow:none;}
selector .elementor-message{color:#F6F7F2;font-size:14px;}"""

def footer():
    newsletter = container({
        "_title": "Newsletter", "content_width": "full",
        "width": px(46, "%"), "width_mobile": px(100, "%"),
        "flex_direction": "column", "flex_gap": {"column": "0", "row": "0", "isLinked": True, "unit": "px", "size": 0},
        "padding": box(0, 0, 0, 0)}, [
        heading4("Suscríbete a nuestro Newsletter"),
        widget("text-editor", {"editor": "<p>Recibe novedades, artículos técnicos y lanzamientos de DMV Premixes.</p>",
                               "text_color": SG, "_element_width": "initial", "_element_custom_width": px(380),
                               "_element_custom_width_mobile": px(100, "%"),
                               **typo("typography", "Archivo", 14, None, 1.6)}),
        widget("form", {
            "_title": "Formulario newsletter",
            "form_name": "Newsletter",
            "form_fields": [{"_id": rid("f"), "custom_id": "email", "field_type": "email",
                             "field_label": "Correo", "placeholder": "Escribe tu correo",
                             "required": "true", "width": "100"}],
            "show_labels": "", "button_text": "Suscríbete", "button_width": "", "button_align": "start",
            "success_message": "¡Gracias! Te suscribiste correctamente.",
            "column_gap": px(0), "row_gap": px(14),
            "field_text_color": WS, "field_background_color": "rgba(0,0,0,0)",
            "field_border_color": CS, "field_border_width": radius(1), "field_border_radius": radius(999),
            **typo("field_typography", "Archivo", 14),
            "button_background_color": RB, "button_text_color": WS,
            "button_background_hover_color": "#1450C6", "button_hover_color": WS,
            "button_border_radius": radius(999),
            "button_text_padding": box(11, 22, 11, 22),
            **typo("button_typography", "Archivo", 14),
            "_element_width": "initial", "_element_custom_width": px(380), "_element_custom_width_mobile": px(100, "%"),
            "_margin": box(26, 0, 0, 0),
            "custom_css": FORM_CSS,
        }),
    ], inner=True)
    explora = container({
        "_title": "Explora", "content_width": "full", "width": px(20, "%"), "width_mobile": px(40, "%"),
        "flex_direction": "column", "padding": box(0, 0, 0, 0)}, [
        heading4("Explora"),
        link_list([("Nosotros", "/nosotros/"), ("Soluciones", "/soluciones/"), ("Industrias", "/industrias/"),
                   ("Calidad", "/calidad/"), ("Blog", "#"), ("Certificaciones", "#"),
                   ("Política de Privacidad", "#"), ("Ubicación", "#")]),
    ], inner=True)
    contacto = container({
        "_title": "Contacto", "content_width": "full", "width": px(26, "%"), "width_mobile": px(52, "%"),
        "flex_direction": "column", "padding": box(0, 0, 0, 0)}, [
        heading4("Contacto"),
        link_list([("contacto@dmvpremixes.com", "mailto:contacto@dmvpremixes.com"),
                   ("WhatsApp +52 55 4357 7104", WHATSAPP),
                   ("Solicitar Asesoría", "/contactanos/")]),
    ], inner=True)
    top = container({
        "_title": "Columnas", "content_width": "full", "width": px(100, "%"),
        "flex_direction": "row", "flex_wrap": "nowrap", "flex_wrap_mobile": "wrap",
        "flex_justify_content": "space-between", "flex_align_items": "flex-start",
        "flex_gap": {"column": "40", "row": "40", "isLinked": True, "unit": "px", "size": 40},
        "flex_gap_mobile": {"column": "24", "row": "40", "isLinked": False, "unit": "px", "size": 24},
        "padding": box(0, 0, 0, 0)}, [newsletter, explora, contacto], inner=True)
    bottom = container({
        "_title": "Logo y derechos", "content_width": "full", "width": px(100, "%"),
        "flex_direction": "row", "flex_direction_mobile": "column",
        "flex_justify_content": "flex-start", "flex_align_items": "center", "flex_align_items_mobile": "flex-start",
        "flex_gap": {"column": "40", "row": "20", "isLinked": False, "unit": "px", "size": 40},
        "margin": box(64, 0, 0, 0), "padding": box(0, 0, 0, 0)}, [
        container({"_title": "Logo", "content_width": "full", "width": px(46, "%"), "width_mobile": px(100, "%"),
                   "padding": box(0, 0, 0, 0)}, [
            widget("image", {"image": {"url": LOGO_WHITE, "id": "", "alt": "DMV Premixes", "source": "library", "size": ""},
                             "image_size": "full", "align": "left", "width": px(160)})], inner=True),
        widget("text-editor", {"editor": "<p>© 2026 DMV Premixes. Todos los derechos reservados.</p>",
                               "text_color": CS, **typo("typography", "Archivo", 13, None, 1.5)}),
    ], inner=True)
    # Envoltura White Sand: el espacio arriba del footer y sus esquinas redondeadas no muestran el fondo del sitio
    return [container({
        "_title": "Footer (envoltura)",
        "content_width": "full", "flex_direction": "column",
        "padding": box(72, 0, 0, 0), "padding_mobile": box(56, 0, 0, 0),
        "background_background": "classic", "background_color": WS,
    }, [container({
        "_title": "Footer",
        "content_width": "boxed", "boxed_width": px(1120), "width": px(100, "%"),
        "flex_direction": "column",
        "flex_gap": {"column": "0", "row": "0", "isLinked": True, "unit": "px", "size": 0},
        "padding": box(72, 24, 36, 24), "padding_mobile": box(56, 16, 32, 16),
        "background_background": "classic", "background_color": CB,
        "border_radius": {"unit": "px", "top": "28", "right": "28", "bottom": "0", "left": "0", "isLinked": False},
    }, [top, bottom], inner=True)])]

# ------------------------------------------------------------------ SECCIONES DE INICIO
def eyebrow(text):
    """Etiqueta de sección con línea superior (como en la estructura del cliente)."""
    return widget("heading", {
        "_title": f"Etiqueta: {text}", "title": text, "header_size": "div", "title_color": RB,
        **typo("typography", "Archivo", 13, None, 1.4),
        "_element_width": "inherit",
        "_border_border": "solid", "_border_width": box(1, 0, 0, 0), "_border_color": "rgba(25,93,228,0.28)",
        "_padding": box(14, 0, 0, 0), "_margin": box(0, 0, 48, 0), "_margin_mobile": box(0, 0, 32, 0)})

def section(title, anchor, elements, extra=None):
    s = {"_title": title, "_element_id": anchor,
         "content_width": "boxed", "boxed_width": px(1120),
         "flex_direction": "column", "flex_align_items": "stretch",
         "flex_gap": {"column": "0", "row": "0", "isLinked": True, "unit": "px", "size": 0},
         "padding": box(72, 24, 72, 24), "padding_mobile": box(56, 16, 56, 16),
         "background_background": "classic", "background_color": WS}
    if extra: s.update(extra)
    return container(s, elements)

PILLARS = [("Conocimiento Técnico", "fas fa-layer-group"),
           ("Soluciones a la medida", "fas fa-sliders-h"),
           ("Capacitación Especializada", "fas fa-graduation-cap"),
           ("Atención Cercana", "fas fa-headset")]

def nosotros():
    pillars = [widget("icon-box", {
        "_title": f"Pilar: {name}",
        "selected_icon": {"value": icon, "library": "fa-solid"}, "position": "top",
        "title_text": name, "description_text": "", "title_size": "div",
        "primary_color": TG, "hover_primary_color": RB, "icon_size": px(28), "icon_space": px(14),
        "title_color": RB, **typo("title_typography", "Archivo", 15, 14, 1.35),
        "text_align": "center",
        "_element_width": "initial", "_element_custom_width": px(22, "%"), "_element_custom_width_mobile": px(46, "%"),
    }) for name, icon in PILLARS]
    return [section("Nosotros", "nosotros", [
        eyebrow("Nosotros"),
        widget("heading", {
            "_title": "Frase (efecto Color Swipe Reveal)",
            "title": 'En <span style="color:#1C1B17">DMV Premixes</span> combinamos conocimiento técnico, experiencia y atención cercana para desarrollar premezclas e ingredientes.',
            "header_size": "h2", "align": "center", "title_color": TG,
            **typo("typography", "Rinter", 48, 28, 1.25, -0.5),
            "typography_font_size_tablet": px(38),
            "_css_classes": "dmv-reveal",
            "_element_width": "initial", "_element_custom_width": px(1000), "_element_custom_width_mobile": px(100, "%"),
            "_flex_align_self": "center"}),
        container({
            "_title": "Pilares", "content_width": "full", "width": px(100, "%"),
            "flex_direction": "row", "flex_wrap": "wrap",
            "flex_justify_content": "center", "flex_align_items": "flex-start",
            "flex_gap": {"column": "24", "row": "32", "isLinked": False, "unit": "px", "size": 24},
            "flex_gap_mobile": {"column": "16", "row": "28", "isLinked": False, "unit": "px", "size": 16},
            "padding": box(0, 0, 0, 0), "margin": box(56, 0, 44, 0), "margin_mobile": box(40, 0, 36, 0),
            "custom_css": "selector{max-width:820px;align-self:center;}"}, pillars, inner=True),
        container({"_title": "Botón", "content_width": "full", "width": px(100, "%"),
                   "flex_direction": "row", "flex_justify_content": "center", "padding": box(0, 0, 0, 0)},
                  [button("Solicita una evaluación técnica", "/contactanos/")], inner=True),
    ])]

CARD_CSS = """/* Tarjeta: el botón siempre abajo, alineado entre tarjetas */
selector .elementor-widget-button{margin-top:auto;}
selector{transition:transform .25s,box-shadow .25s;}
selector:hover{transform:translateY(-4px);box-shadow:0 2px 4px rgba(28,27,23,.04),0 20px 48px rgba(28,27,23,.10);}"""

SOLUTIONS = [("01", "Premezclas y<br>Fortificación", "Vitaminas, minerales, aminoácidos y formulaciones personalizadas.", "Ver Premezclas"),
             ("02", "Enzimas y<br>Mejorantes", "Aplicaciones en harinas, panificación y procesos alimentarios.", "Ver Enzimas"),
             ("03", "Aditivos e<br>Ingredientes", "Ingredientes funcionales según la aplicación.", "Ver Ingredientes")]

def soluciones():
    cards = [container({
        "_title": f"Tarjeta {num}", "content_width": "full",
        "width": px(30, "%"), "width_mobile": px(100, "%"), "_flex_size": "grow",
        "flex_direction": "column", "flex_align_items": "flex-start",
        "flex_gap": {"column": "0", "row": "0", "isLinked": True, "unit": "px", "size": 0},
        "min_height": px(320), "min_height_mobile": px(260),
        "padding": box(24, 24, 24, 24),
        "background_background": "classic", "background_color": "#FFFFFF",
        "border_border": "solid", "border_width": radius(1), "border_color": SG, "border_radius": radius(18),
        "box_shadow_box_shadow_type": "yes",
        "box_shadow_box_shadow": {"horizontal": 0, "vertical": 8, "blur": 24, "spread": 0, "color": "rgba(28,27,23,0.06)"},
        "custom_css": CARD_CSS,
    }, [
        widget("heading", {"title": num, "header_size": "div", "title_color": CS, "_margin": box(0, 0, 22, 0),
                           **typo("typography", "Archivo", 12)}),
        widget("heading", {"title": title, "header_size": "h3", "title_color": RB, "_margin": box(0, 0, 10, 0),
                           **typo("typography", "Rinter", 21, 20, 1.2)}),
        widget("text-editor", {"editor": f"<p>{desc}</p>", "align": "left", "text_color": TG, "_margin": box(0, 0, 24, 0),
                               **typo("typography", "Archivo", 14, None, 1.5)}),
        button(btn, "/soluciones/", size=14, pad=(12, 26)),
    ], inner=True) for num, title, desc, btn in SOLUTIONS]
    return [section("Soluciones", "soluciones", [
        eyebrow("Soluciones"),
        container({
            "_title": "Encabezado", "content_width": "full", "width": px(100, "%"),
            "flex_direction": "row", "flex_direction_mobile": "column", "flex_align_items": "flex-start",
            "flex_gap": {"column": "40", "row": "16", "isLinked": False, "unit": "px", "size": 40},
            "padding": box(0, 0, 0, 0), "margin": box(0, 0, 48, 0), "margin_mobile": box(0, 0, 32, 0)}, [
            widget("heading", {"title": "Nuestro<br>portafolio", "header_size": "h2", "title_color": CB,
                               "_element_width": "initial", "_element_custom_width": px(40, "%"),
                               "_element_custom_width_mobile": px(100, "%"),
                               **typo("typography", "Rinter", 38, 30, 1.12, -0.5)}),
            widget("text-editor", {
                "editor": "<p>En DMV Premixes desarrollamos soluciones de premezclas personalizadas que combinan conocimiento técnico, calidad de ingredientes y precisión de formulación para responder a los requerimientos nutricionales y funcionales de nuestros clientes.</p>",
                "align": "left", "text_color": TG, "_flex_size": "grow",
                **typo("typography", "Archivo", 16, 15, 1.6)}),
        ], inner=True),
        container({
            "_title": "Tarjetas", "content_width": "full", "width": px(100, "%"),
            "flex_direction": "row", "flex_direction_mobile": "column",
            "flex_align_items": "stretch", "flex_wrap": "nowrap",
            "flex_gap": {"column": "22", "row": "18", "isLinked": False, "unit": "px", "size": 22},
            "padding": box(0, 0, 0, 0)}, cards, inner=True),
        container({"_title": "Botón", "content_width": "full", "width": px(100, "%"),
                   "flex_direction": "row", "flex_justify_content": "center",
                   "padding": box(0, 0, 0, 0), "margin": box(40, 0, 0, 0)},
                  [button("Habla con un especialista", "/contactanos/")], inner=True),
    ], extra={
        # Brillo azul suave detrás de las tarjetas (sin bandas: se desvanece a White Sand)
        "background_background": "gradient", "background_color": "rgba(25,93,228,0.14)",
        "background_color_stop": px(0, "%"), "background_color_b": WS, "background_color_b_stop": px(62, "%"),
        "background_gradient_type": "radial", "background_gradient_position": "center center",
    })]

if __name__ == "__main__":
    save("01-hero.json", "DMV - Hero", "container", hero())
    save("02-header.json", "DMV - Header", "header", header())
    save("03-footer.json", "DMV - Footer", "footer", footer())
    save("04-nosotros.json", "DMV - Nosotros", "container", nosotros())
    save("05-soluciones.json", "DMV - Soluciones", "container", soluciones())
    # Fragmento suelto: código de la franja de logos para pegar en un widget HTML
    frag = ROOT / "elementor/fragmentos"; frag.mkdir(parents=True, exist_ok=True)
    (frag / "franja-logos.html").write_text(marquee_html() + "\n")
    print("OK fragmentos/franja-logos.html")

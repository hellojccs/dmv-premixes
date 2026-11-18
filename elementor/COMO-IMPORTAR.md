# Cómo importar una plantilla en Elementor (prueba: Hero)

Archivo: `plantillas/01-hero-prueba.json`

**Esto no cambia tu sitio publicado.** La plantilla se guarda en tu biblioteca y la usamos en una página en borrador.

## 0. Antes (recomendado)
Sube la fuente Rinter para que los títulos se vean bien:
*Elementor → Custom Fonts → Add New* → nombre `Rinter` → peso **400** → sube `Rinter-Regular.woff2`, `.woff` y `.ttf` (carpeta `brand/fonts/`) → **Publicar**.
Si no lo haces, el título se verá con otra fuente; el resto funciona igual.

## 1. Importar la plantilla
1. En el panel de WordPress ve a **Plantillas → Plantillas guardadas** (en algunas versiones: *Elementor → Plantillas*).
2. Clic en **Importar plantillas** (botón arriba).
3. Elige el archivo `01-hero-prueba.json` → **Importar ahora**.
4. Aparecerá en la lista como **"DMV - Hero (prueba)"**.

## 2. Usarla en una página de prueba
1. **Páginas → Añadir nueva**. Título: `Prueba hero`.
2. Clic en **Editar con Elementor**.
3. En el lienzo, clic en el ícono de **carpeta** (Añadir plantilla) → pestaña **Mis plantillas** → **DMV - Hero (prueba)** → **Insertar**.
   Si pregunta si quieres importar la configuración del documento → **No**.
4. Guarda como **borrador**: flecha junto a *Publicar* → *Guardar borrador*.
5. Clic en el ícono del **ojo** (Vista previa) para verla como visitante.

## 3. Prueba editar
- Clic en el título → cambia el texto en el panel izquierdo.
- Clic en un botón → pestaña *Estilo* → cambia colores o bordes.
- Revisa la vista móvil con el ícono de dispositivos (abajo a la izquierda o arriba).

## 4. Cuéntame
Mándame una captura de cómo se ve y qué fue distinto al prototipo. Con eso ajusto las siguientes plantillas.

## Si algo falla
- **No aparece el logo:** clic en el logo → *Elegir imagen* → selecciona el logo blanco de tu biblioteca de medios.
- **Error al importar:** mándame el mensaje exacto (captura).
- **Para borrar la prueba:** elimina la página "Prueba hero" y la plantilla en *Plantillas guardadas*. Nada más se ve afectado.

## Qué incluye esta prueba (y qué no)
- ✅ Fondo azul degradado, logo, título, texto, 2 botones; versión móvil.
- ⏳ La franja animada de logos de clientes y el **header** vienen en la siguiente prueba (el header se monta con *Theme Builder* de Elementor Pro).

---

# Prueba 2: Header (`plantillas/02-header.json`)

El header se monta con **Theme Builder** (Elementor Pro) para que aparezca en todas las páginas.
En esta prueba **solo se mostrará en la página "Prueba hero"**; el resto de tu sitio sigue con el header actual.

## 1. Revisa tu menú de WordPress
*Apariencia → Menús* (o *Apariencia → Editor → Navegación*): confirma que tu menú principal tiene **Nosotros, Soluciones, Industrias, Calidad**.
Opcional: para el desplegable de "Nosotros", arrastra páginas un poco a la derecha, debajo de "Nosotros".

## 2. Importa el header
*Plantillas → Plantillas guardadas → Importar plantillas* → `02-header.json` → **Importar ahora**.

## 3. Elige tu menú
1. *Plantillas → Theme Builder* → **Header** → "DMV - Header" → **Editar con Elementor**.
2. Clic en el menú (al centro de la barra) → en el panel izquierdo, campo **Menú** → elige tu menú principal.
3. **Actualizar** / **Publicar**.

> En el editor el header puede verse "pegado" arriba del lienzo: es normal, es porque es flotante.

## 4. Muéstralo solo en la página de prueba
1. Abre la página **Prueba hero** en WordPress → en *Visibilidad* elige **Privada** → **Publicar**.
   (Privada = solo tú la ves con tu sesión iniciada.)
2. Vuelve al header en Elementor → flecha junto a *Publicar* → **Condiciones de visualización** →
   **Añadir condición** → *Incluir* → *Singular* → *Páginas* → **Prueba hero** → **Guardar y cerrar**.

Como esa condición es más específica que "Todo el sitio", **solo esa página** usa el header nuevo.

## 5. Revisa
Abre la página *Prueba hero* (con tu sesión iniciada) en computadora y en celular:
- **Dos barras flotantes** con efecto vidrio: a la izquierda el **logo completo** y el menú (texto blanco); a la derecha **WhatsApp + Contáctanos**.
- Al pasar el mouse por el menú: fondo **Royal Blue al 50%**.
- Al hacer scroll: el logo se reduce al **símbolo en círculo azul** y ambas barras se vuelven **Carbon Black** translúcidas.
- Botón **WhatsApp** verde (gris al pasar el mouse).
- En celular: izquierda logo + menú hamburguesa; derecha WhatsApp.

> Si ya habías importado una versión anterior del header, borra la anterior en *Plantillas guardadas* e importa esta.

## Cuando lo apruebes
En las condiciones del header nuevo cambia la condición a **Todo el sitio**, y en el header viejo elimina su condición (o muévelo a borrador).

## Notas
- WhatsApp abre el chat con **+52 55 4357 7104**. Para cambiarlo: clic en el ícono → *Enlace*.
- En celular el botón "Contáctanos" se oculta; si quieres que aparezca dentro del menú hamburguesa, agrega la página *Contáctanos* a tu menú de WordPress.
- El header flota encima del contenido. En páginas sin hero azul lo ajustaremos al diseñar las páginas internas.

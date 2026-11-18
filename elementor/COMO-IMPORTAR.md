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

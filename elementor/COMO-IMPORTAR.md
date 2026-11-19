# Cómo importar las plantillas en Elementor

## Prueba 1: Hero

Archivo: `plantillas/01-hero.json` (incluye la franja animada de logos de clientes)

**Esto no cambia tu sitio publicado.** La plantilla se guarda en tu biblioteca y la usamos en una página en borrador.

## 0. Antes (recomendado)
Sube la fuente Rinter para que los títulos se vean bien:
*Elementor → Custom Fonts → Add New* → nombre `Rinter` → peso **400** → sube `Rinter-Regular.woff2`, `.woff` y `.ttf` (carpeta `brand/fonts/`) → **Publicar**.
Si no lo haces, el título se verá con otra fuente; el resto funciona igual.

## 1. Importar la plantilla
1. En el panel de WordPress ve a **Plantillas → Plantillas guardadas** (en algunas versiones: *Elementor → Plantillas*).
2. Clic en **Importar plantillas** (botón arriba).
3. Elige el archivo `01-hero.json` → **Importar ahora**.
4. Aparecerá en la lista como **"DMV - Hero"**.

## 2. Usarla en una página de prueba
1. **Páginas → Añadir nueva**. Título: `Prueba hero`.
2. Clic en **Editar con Elementor**.
3. En el lienzo, clic en el ícono de **carpeta** (Añadir plantilla) → pestaña **Mis plantillas** → **DMV - Hero** → **Insertar**.
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
- ✅ Franja animada de logos de clientes (marcas **ficticias de ejemplo**, ver `brand/clientes-ejemplo/`).

### Actualizar el hero que ya importaste
1. En *Plantillas guardadas* borra "DMV - Hero (prueba)" e importa `01-hero.json`.
2. En la página *Prueba hero* → Editar con Elementor → clic derecho sobre el hero → **Eliminar**.
3. Ícono de carpeta → *Mis plantillas* → **DMV - Hero** → **Insertar** → **Actualizar**.
4. ⚙️ *Configuración de página* → activa **Ocultar título** (si no lo habías hecho).

### Cambiar los logos de clientes (cuando lleguen los reales)
Por ahora la franja es un widget **HTML**. Cuando tengas los logos reales mándamelos y te genero la versión final
(o una con widget de *Carrusel de imágenes* para que puedas cambiarlos tú desde la biblioteca de medios).

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
- Al hacer scroll: el logo se reduce al **símbolo en círculo azul**, los enlaces del menú se ocultan y aparece un botón **⋮** que abre el menú; ambas barras se vuelven **Carbon Black** translúcidas.
- Botón **WhatsApp** verde (gris al pasar el mouse).
- En celular: izquierda logo + menú hamburguesa; derecha WhatsApp.

> Si ya habías importado una versión anterior del header, borra la anterior en *Plantillas guardadas* e importa esta.

## Cuando lo apruebes
En las condiciones del header nuevo cambia la condición a **Todo el sitio**, y en el header viejo elimina su condición (o muévelo a borrador).

## Notas
- WhatsApp abre el chat con **+52 55 4357 7104**. Para cambiarlo: clic en el ícono → *Enlace*.
- En celular el botón "Contáctanos" se oculta; si quieres que aparezca dentro del menú hamburguesa, agrega la página *Contáctanos* a tu menú de WordPress.
- El header flota encima del contenido. En páginas sin hero azul lo ajustaremos al diseñar las páginas internas.

---

# Prueba 3: Footer (`plantillas/03-footer.json`)

Igual que el header, el footer se monta con **Theme Builder** para que aparezca en todas las páginas.

## 1. Importa
*Plantillas → Plantillas guardadas → Importar plantillas* → `03-footer.json` → **Importar ahora**.
Aparece como **"DMV - Footer"** (tipo *Footer*).

## 2. Muéstralo solo en la página de prueba
*Plantillas → Theme Builder → Footer* → "DMV - Footer" → **Editar con Elementor** → **Publicar** →
**Añadir condición** → *Incluir* → *Singular* → *Páginas* → **Prueba hero** → **Guardar y cerrar**.

## 3. Revisa en la página *Prueba hero*
- Fondo **Carbon Black** con esquinas superiores redondeadas.
- **Newsletter**: título, texto, campo de correo redondeado y botón **Suscríbete**.
- **Explora** y **Contacto** (correo, WhatsApp +52 55 4357 7104, Solicitar Asesoría).
- Abajo: logo blanco y "© 2026 DMV Premixes. Todos los derechos reservados."
- En celular: Newsletter arriba a todo lo ancho; Explora y Contacto lado a lado.

## Notas
- **Newsletter:** por defecto envía un correo al administrador de WordPress con cada suscripción.
  Para cambiarlo: clic en el formulario → *Acciones después de enviar* (puedes conectar Mailchimp u otro).
  Haz una prueba suscribiendo tu correo.
- **Enlaces:** Explora usa tus páginas (/nosotros/, /soluciones/, /industrias/, /calidad/). Blog, Certificaciones,
  Política de Privacidad y Ubicación quedan en `#` hasta que existan; se cambian con clic en la lista → cada elemento → *Enlace*.
- El correo **contacto@dmvpremixes.com** es de ejemplo: confírmame el real.

---

# Efecto "Color Swipe Reveal" (texto que se revela al hacer scroll)

Archivo: `fragmentos/color-swipe-reveal.html`. Se instala **una sola vez** y sirve para cualquier texto.

## 1. Instala el código (una vez)
1. *Elementor → Código personalizado* (Custom Code) → **Añadir nuevo**.
2. Título: `Color Swipe Reveal`.
3. Abre `color-swipe-reveal.html` con un editor de texto, copia **todo** y pégalo.
4. **Ubicación:** *Fin del body* (`</body> - End`).
5. **Publicar** → condición **Todo el sitio** → **Guardar y cerrar**.

## 2. Activa el efecto en un texto
1. Edita la página con Elementor y selecciona el widget del texto (Título o Editor de texto).
2. *Avanzado → Clases CSS* → escribe `dmv-reveal`.
3. **Actualizar**.

## 3. Revisa
El efecto se ve en la **página publicada / vista previa**, no dentro del editor (ahí el texto se ve normal y lo puedes editar como siempre).
Al bajar, cada palabra pasa de azul translúcido desenfocado a su color final.

> Si alguien tiene activada la opción "reducir movimiento" en su dispositivo, el texto se muestra normal, sin animación.

---

# Secciones de la página de Inicio

| Archivo | Sección |
|---|---|
| `04-nosotros.json` | Nosotros: etiqueta, frase con efecto **Color Swipe Reveal** (clase `dmv-reveal` ya incluida), 4 pilares y botón |
| `05-soluciones.json` | Soluciones: etiqueta, título + texto, 3 tarjetas de igual altura con botón alineado abajo, botón final |

## 1. Importa
*Plantillas → Plantillas guardadas → Importar plantillas* → importa `04-nosotros.json` y `05-soluciones.json`.

## 2. Reemplaza tus secciones actuales
1. Abre **Inicio** → **Editar con Elementor** → abre el **Navegador** (ícono de capas o Ctrl/Cmd + I).
2. Clic derecho sobre tu sección de **Nosotros** actual → **Eliminar**. Haz lo mismo con tu sección de **portafolio**.
3. Debajo del hero: ícono de **carpeta** → *Mis plantillas* → **DMV - Nosotros** → **Insertar**.
4. Repite con **DMV - Soluciones**.
5. En el Navegador, arrastra las secciones para que el orden sea: **Hero → Nosotros → Soluciones**.
6. **Actualizar**.

> Los íconos de los pilares se cambian con clic en el pilar → *Ícono* (puedes elegir otro o subir un SVG, por ejemplo el símbolo DMV).
> Los botones ya enlazan a /contactanos/ y /soluciones/; el hero ya enlaza a estas secciones (#soluciones).

## 3. Footer actualizado
`03-footer.json` ahora trae su propio fondo White Sand alrededor, para que **no se asome el azul** del fondo del sitio arriba del footer.
- Opción A: borra el footer actual en *Plantillas guardadas*, importa el nuevo y vuelve a poner su condición.
- Opción B (rápida): en tu footer actual → selecciona el contenedor principal → *Avanzado → Margen* → arriba **0**.

## Recomendado
*Elementor → Configuración del sitio → Fondo* → color **White Sand (#F6F7F2)**.
Hoy el fondo general es Royal Blue: cualquier espacio sin fondo propio se ve como una banda azul.

---

# Flechas del carrusel (círculos Royal Blue por fuera de las tarjetas)

Archivo: `fragmentos/flechas-carrusel.css`
1. Selecciona el widget **Carrusel anidado** → *Avanzado* → **CSS personalizado**.
2. Pega todo el contenido del archivo → **Actualizar**.

- Computadora: flechas a los lados, fuera de las tarjetas.
- Tablet y celular: centradas debajo de las tarjetas.
- La flecha se ve más clara cuando no hay más tarjetas en esa dirección.

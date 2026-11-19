# Revisión completa — dmvpremixes.com (Inicio)

Fecha: 19 nov 2026 · Revisado en computadora (1440 px), tablet (1024 px) y celular (iPhone 13).

## ✅ Funciona bien
- Header: 2 barras, logo completo → símbolo al hacer scroll, menú se oculta y aparece ⋮, WhatsApp.
- Color Swipe Reveal en Nosotros (15/15 palabras se revelan).
- Carrusel de Soluciones: 3 tarjetas, misma altura, botones alineados, flechas Royal Blue.
- Industrias: tarjetas apiladas, máscara del símbolo DMV, indicador 1-2-3.
- Footer, franja de logos animada.
- **Sin desborde lateral** en ningún tamaño · sin errores de JavaScript propios.
- Velocidad: ~3 s de carga, 49 archivos, ~730 KB.

## 🔴 Crítico
- [ ] **La fuente Rinter NO carga para los visitantes.** Tu WordPress tiene la "Dirección de WordPress" en `http://` y el navegador bloquea la fuente por "contenido mixto". Los títulos se ven en Archivo (o en otra fuente) para todos los que no tengan Rinter instalada en su computadora.
  1. *Ajustes → Generales* → **Dirección de WordPress (URL)**: `https://dmvpremixes.com` (igual que "Dirección del sitio") → Guardar.
  2. *Elementor → Herramientas → Reemplazar URL*: de `http://dmvpremixes.com` a `https://dmvpremixes.com` → Reemplazar.
  3. *Elementor → Herramientas → General* → **Regenerar archivos y datos**.
  4. *Elementor → Custom Fonts → Rinter*: sube también el **.woff2** (hoy solo hay .woff y .otf).
- [ ] **Google no puede indexar el sitio** (`noindex, nofollow`). Si es intencional mientras está en construcción, OK; al lanzar: *Ajustes → Lectura* → desmarca "Disuadir a los motores de búsqueda".
- [ ] **Pilares de Nosotros: los 4 dicen "Conocimiento Técnico".** Cambia 3 títulos: Soluciones a la medida · Capacitación Especializada · Atención Cercana.

## 🟠 Importante
- [ ] **Botones sin destino (`#`)**: hero *Ver Soluciones* y *Consulta una asesoría*; *Explorar más* (carrusel); *Conoce más* (Industrias).
  - Sección Soluciones → *Avanzado → ID CSS*: `soluciones` → hero *Ver Soluciones* → `#soluciones`.
  - *Consulta una asesoría* → `/contactanos/`. *Explorar más* → `/soluciones/`. *Conoce más* → `/industrias/`.
- [ ] **Celular: el header tapa el logo del hero.** Hero → vista celular → *Avanzado → Relleno arriba: 130*.
- [ ] **Páginas de prueba publicadas**: *Pagina Prueba*, *Mantenimiento*, *Sample Page* → pasarlas a **Borrador**.
- [ ] **Carrusel: tarjetas 4 y 5 repiten "Premezclas y Fortificación"**. Cambiar contenido o eliminarlas.
- [ ] **Estructura de títulos (SEO)**: no hay **H1**. Hero *Precisión en cada formulación* → etiqueta **H1**. En el carrusel los números "01…05" son H2 → cambiarlos a **div** o **p**.

## 🟡 Mejoras
- [ ] **Texto alternativo (alt)** en imágenes: logo del hero, íconos de pilares, fotos de Industrias, logo del footer (*Biblioteca de medios → imagen → Texto alternativo*).
- [ ] **Fondo del hero** `BCG-scaled.png` pesa **297 KB** → exportar en **WebP o JPG** (~60–90 KB).
- [ ] **Descripción para Google y redes** (meta description / imagen al compartir): instalar *Yoast SEO* o *Rank Math*.
- [ ] Sección Industrias: **relleno abajo 72**; borde Tarjeta 2 en Royal Blue; botón Tarjeta 3 en azul suave.
- [ ] Footer: links *Blog, Certificaciones, Política de Privacidad, Ubicación* en `#`.

## ⏳ Contenido pendiente del cliente
- [ ] 3 fotos de Industrias (hoy *placeholder*).
- [ ] Logos reales de clientes (hoy marcas **ficticias** visibles en el sitio).
- [ ] Correo real de contacto (hoy `contacto@dmvpremixes.com` de ejemplo).
- [ ] Textos definitivos.

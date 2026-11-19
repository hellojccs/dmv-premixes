# Arreglos rápidos — Inicio (títulos y botones)

Todo se hace en **Inicio → Editar con Elementor**. Al final, **Actualizar**.
Tip: abre el **Navegador** (Ctrl/Cmd + I) para encontrar cada elemento más rápido.

## 1. Títulos (SEO)
- **Hero — "Precisión en cada formulación"**: clic en el título → *Contenido → Etiqueta HTML* → **H1**.
  (En el sitio publicado ya parece estar como H1; solo confírmalo. Debe haber **un solo H1** en la página.)
- **Portafolio — los números "01, 02, 03, 04, 05"**: hoy son **H2**. Clic en cada número → *Etiqueta HTML* → **div**.
  Así Google lee como títulos los nombres de las soluciones y no los números.

## 2. Botones que hoy no llevan a ningún lado (`#`)

### Primero: dale nombre a la sección del portafolio
Selecciona el contenedor de la sección **Nuestro portafolio** (el de afuera) → *Avanzado* → **ID CSS** → `soluciones`.
(Sin el `#`. Esto permite que un botón te lleve directo a esa sección.)

### Luego cambia el enlace de cada botón
Clic en el botón → *Contenido → Enlace*:

| Dónde | Botón | Enlace nuevo |
|---|---|---|
| Hero | Ver Soluciones | `#soluciones` |
| Hero | Consulta una asesoría | `/contactanos/` |
| Portafolio (las 5 tarjetas) | Explorar más | `/soluciones/` |
| Industrias (las 3 tarjetas) | Conoce más | `/industrias/` |

> En el carrusel del portafolio, cada tarjeta tiene su propio botón: hay que cambiar los 5.

### Los que se quedan en `#` por ahora (a propósito)
- **Carrito del header**: se conecta cuando montemos la tienda con WooCommerce.
- **Footer → Blog, Certificaciones, Política de Privacidad, Ubicación**: esas páginas todavía no existen.
  Cuando tengas la dirección, *Ubicación* puede llevar a Google Maps.

## 3. Revisa
Abre la página publicada (o la vista previa) y haz clic en cada botón:
- *Ver Soluciones* baja suavemente hasta **Nuestro portafolio** (el header flotante no debe tapar el título).
- Los demás abren su página.

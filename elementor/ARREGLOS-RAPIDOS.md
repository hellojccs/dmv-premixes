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

---

# Espaciado único en Inicio (`fragmentos/espaciado-inicio.css`)

## Qué estaba pasando (valores leídos del CSS publicado)
| Sección | Arriba / abajo (compu · celular) | Lados | Otros |
|---|---|---|---|
| Nosotros (frase + pilares) | 20 · 20, con altura mínima 60 % de la pantalla | 20 | la frase tenía 60 extra arriba |
| Portafolio | 20 · 60, con altura mínima 80 % de la pantalla | 20 | tarjetas del carrusel con 30 extra arriba y abajo |
| Industrias | 72 · 56 | 24 · 16 | 72 extra debajo de las tarjetas en celular |
| Más que ingredientes | 72 · 56 | 24 · 16 | cita con 26 / 28 |
| Hero (tablet) | relleno 65 = lo que sube el hero → el contenido queda bajo el header | | en celular solo 20 abajo |

Además, el espacio entre título, texto y contenido dependía del espacio automático de Elementor, distinto en cada sección.

## Escala nueva (computadora · tablet · celular)
- Sección, arriba y abajo: **72 · 64 · 56**. A los lados: **24 · 24 · 16**. Sin altura mínima.
- Título → texto: **16 · 16 · 12**
- Encabezado → contenido (pilares, carrusel, tarjetas): **48 · 40 · 32**
- Contenido → botones: **32 · 32 · 24** · entre botones **12**

## Cómo aplicarlo
1. **Inicio → Editar con Elementor** → ⚙️ (Configuración de página) → **Avanzado → CSS personalizado**.
2. Pega todo `espaciado-inicio.css` → **Actualizar**.
3. *Elementor → Herramientas → Regenerar archivos y datos* si no ves el cambio, y recarga sin caché.

> No hace falta tocar los rellenos sección por sección: el CSS manda sobre lo que diga el panel.
> Si borras y vuelves a crear una sección, cambia su ID y hay que actualizar el archivo (avísame).

## Ajuste a mano recomendado
En **Más que ingredientes**, los botones están **fuera** de la columna de texto (quedan debajo de todo, también de la foto).
Navegador → arrastra el contenedor de los botones **dentro** de la columna del texto, debajo de la cita.

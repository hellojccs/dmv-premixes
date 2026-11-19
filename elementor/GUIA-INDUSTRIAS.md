# Guía: sección "Industrias y Aplicaciones" (tarjetas apiladas)

Referencia visual: prototipo → sección *Industrias y Aplicaciones*.
Código del efecto: `fragmentos/tarjetas-apiladas.html`.

> ⚠️ Reglas para que el efecto funcione
> - **No** uses *Efectos de movimiento → Sticky* de Elementor en las tarjetas (el código ya las fija).
> - **No** pongas *Animación de entrada* en las tarjetas.
> - El contenedor de la sección debe tener **Desbordamiento: Predeterminado** (no "Oculto").
> - El efecto se ve en la **vista previa / página publicada**, no dentro del editor.

---

## FASE 1 — Código + encabezado de la sección

### 1.1 Instala el código (una sola vez)
*Elementor → Código personalizado → Añadir nuevo*
- Título: `Tarjetas apiladas`
- Pega **todo** `tarjetas-apiladas.html`
- Ubicación: **Fin del body** → **Publicar** → condición **Todo el sitio**

### 1.2 Contenedor de la sección
En **Inicio**, debajo de Soluciones, agrega un **Contenedor**:
- *Diseño*: Ancho del contenido **En caja**, Ancho **1120**; Dirección **Columna**
- *Estilo → Fondo*: **White Sand (#F6F7F2)**
- *Avanzado*: Relleno **72 / 24 / 72 / 24** (celular **56 / 16 / 56 / 16**); ID CSS: `industrias`

### 1.3 Encabezado (dentro del contenedor)
- **Título** (H2): *Soluciones para cada industria* — centrado, **Rinter 38** (celular 30), **Carbon Black**
- **Editor de texto**: *Cada proceso productivo tiene requerimientos específicos. Te ayudamos a elegir los ingredientes y las soluciones técnicas que mejor se adaptan a tu aplicación.* — centrado, **Archivo 16**, **Taupe Grey**; *Avanzado → Ancho*: personalizado **640 px**; *Alinear a sí mismo*: centro

---

## FASE 2 — La primera tarjeta

### 2.1 Contenedor "Tarjetas"
Dentro de la sección, agrega un **Contenedor**:
- *Diseño*: Dirección **Columna**; **Espacio entre elementos: 180** (celular **16**)
- *Avanzado*: Margen arriba **56** (celular 32); **Clases CSS: `dmv-stack`**

### 2.2 Tarjeta 1 (dentro de "Tarjetas")
Agrega un **Contenedor**:
- *Diseño*: Dirección **Fila** (celular **Columna**); Altura mínima **540** (celular vacío); Espacio entre elementos **0**
- *Estilo*: Fondo **Blanco**; Borde sólido **1 px** **Soft Grey (#E9E6DF)**; Radio **32** (celular 24); Sombra suave
- *Avanzado*: Relleno **14** (celular 10); **Clases CSS: `dmv-stack-card`**

### 2.3 Foto (dentro de la tarjeta)
Agrega un **Contenedor**:
- *Diseño*: Ancho **56%** (celular **100%**); Justificar **Centro**; Alinear **Centro**; Altura mínima celular **240**
- *Estilo*: Fondo **White Sand**; Radio **24** (celular 18)

Dentro, un widget **Imagen** con tu foto:
- *Estilo*: Ancho **80%**, Ancho máximo **440 px** (celular: Ancho **64%**)
- *Avanzado*: **Clases CSS: `dmv-shape`** → la foto se recorta con la forma del símbolo DMV

### 2.4 Texto (dentro de la tarjeta, al lado de la foto)
Agrega un **Contenedor**:
- *Diseño*: Ancho **44%** (celular **100%**); Dirección **Columna**; Justificar **Inicio**
- *Avanzado*: Relleno **56 / 44 / 36 / 44** (celular **24 / 18 / 20 / 18**); **Clases CSS: `dmv-stack-content`**
  (aquí aparece solo el indicador de 3 símbolos DMV)

Dentro:
- **Título** (H3): *Alimentos y Panificación* — **Rinter 44** (celular 30), **Royal Blue**, margen abajo 16
- **Editor de texto**: *Premezclas, enzimas y mejorantes que aportan consistencia, volumen y vida de anaquel a harinas, pan y productos de panificación.* — **Archivo 16**, **Taupe Grey**, alineado a la izquierda
- **Botón**: *Conoce más*
  - Fondo **rgba(25,93,228,0.08)** · texto **Royal Blue** · hover fondo **rgba(25,93,228,0.16)**
  - **Rinter 15** · Radio **999** · Relleno **14 / 26 / 10 / 26** (el 14/10 centra Rinter)
  - Margen arriba **28**; *Alinear a sí mismo*: **Inicio**

---

## FASE 3 — Tarjetas 2 y 3

### Tarjeta 2: Bebidas (Royal Blue, foto a la derecha)
Clic derecho en la Tarjeta 1 → **Duplicar**, y en la copia:
- Tarjeta: Fondo **Royal Blue**, borde **Royal Blue**; **Clases CSS: `dmv-stack-card dmv-dark`**
- Contenedor Foto: Fondo **rgba(246,247,242,0.14)**; *Avanzado → Orden*: **Último** (celular: **Primero**)
- Título: *Bebidas* — color **White Sand**
- Texto: *Fortificación con vitaminas y minerales estables y de fácil dispersión para bebidas listas para tomar, polvos y concentrados.* — color **rgba(246,247,242,0.86)**
- Botón: fondo **White Sand**, texto **Royal Blue**, hover fondo **Blanco**
- Foto de bebidas

### Tarjeta 3: Nutrición Animal (blanca)
Duplica la **Tarjeta 1** y colócala al final:
- Título: *Nutrición Animal*
- Texto: *Premezclas vitamínicas y minerales a la medida para alimento balanceado de aves, cerdos, rumiantes y mascotas.*
- Foto de nutrición animal

**Actualizar** y revisar en la vista previa.

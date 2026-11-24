# Registro de videos: Videoteca Igor teechah

Fuente de verdad de qué video pertenece a qué bloque y en qué orden. **Nunca se mezclan videos entre bloques.** Orden de los canales en la web: Bloque 1, Formularios, Bloque 2, Bloque 3.
`index.html` tiene una sección `BLOQUES` que debe coincidir siempre con este archivo.

- Repositorio: https://github.com/igorhermoso1/Video-juritecnia
- Release: `Grabaciones` (tag `v1.0`). Todos los videos están en esta misma release.
- Enlace de cada video: `https://github.com/igorhermoso1/Video-juritecnia/releases/download/v1.0/<archivo>`
- Plataforma de alumnos: https://igorhermoso1.github.io/Formaci-n_Juritecnia/

## Archivos del proyecto

| Archivo | Para qué sirve |
|---------|----------------|
| `index.html` | La página de la videoteca |
| `logo.webp` | Logo "Igor-Movies" que se ve junto al título (debe estar en la misma carpeta que `index.html`) |
| `VIDEOS.md` | Este registro |
| `faststart.py` | Prepara cada video antes de subirlo para que arranque al instante (ver abajo) |

## Cómo trabajamos

1. Subes los videos nuevos a la release **tal cual salen de OBS** (no hace falta renombrarlos ni prepararlos).
2. Me dices qué videos son y a qué bloque van (o los dejas en `webs/video/`).
3. Yo los paso por `faststart.py` y los sustituyo en la release con el mismo nombre. Después actualizo este registro y `index.html` (título, archivo y **duración**), sin mover videos de un bloque a otro.

### Por qué tardaban en cargar y cómo se arregla

Un MP4 lleva un **índice** (la caja `moov`: dónde está cada segundo de imagen y sonido). OBS lo escribe **al final** del archivo, porque no sabe cuánto durará la grabación hasta que paras. El navegador necesita ese índice para empezar: con el índice al final tiene que pedir el principio, saltar al final, descargar el índice (hasta 5 MB en las clases de hora y media) y volver. Contra GitHub, cada salto pasa además por una redirección. Medido el 2026-11-18: **11,5 s** para arrancar `Formularios_correccion.mp4`.

La solución es mover el índice al principio («faststart»). No se recomprime nada: la imagen, el sonido y la calidad quedan idénticos, solo cambia el orden de las piezas.

```
python faststart.py original.mp4 listo.mp4
```

El script comprueba él mismo que el resultado está bien. Si tienes ffmpeg, es lo mismo que `ffmpeg -i original.mp4 -c copy -movflags +faststart listo.mp4`.

**Estado de los videos ya subidos:** los 10 pasaron por `faststart.py` el 2026-11-18 y se volvieron a subir con el mismo nombre. Se comprobaron todos los trozos de cada archivo y, en GitHub, que el índice va delante. Medido en frío desde la web publicada: `Formularios_correccion.mp4` arranca en **4 s** (antes 11,5 s) y salta a cualquier minuto en menos de 1 s. Los segundos que quedan son la descarga del propio índice: 3-5 MB en las clases largas.

La web ayuda además en dos cosas: se conecta a GitHub nada más abrirse (`preconnect`) y, al pasar el ratón o el foco por una cinta, empieza a descargar su índice.

---

## Bloque 1  (id 1)

- **Origen:** Release `Grabaciones` (v1.0). Los 5 primeros videos subidos; la Corrección Pokédex pasó al Bloque 2 el 2026-11-19.
- **Estado:** cerrado, salvo que se indique lo contrario.

| Orden | Título en la web | Archivo | Duración | Tamaño | Alta |
|------:|------------------|---------|---------:|-------:|------|
| 1 | Boceto general | `boceto_general.mp4` | 37:30 | 191 MB | 2026-11-18 |
| 2 | Cuarto ejercicio | `Cuarto.ejercicio.mp4` | 17:52 | 92.3 MB | 2026-11-18 |
| 3 | Popurri | `Popurri.mp4` | 42:35 | 164 MB | 2026-11-18 |
| 4 | Primer ejercicio | `primerEjercicio.mp4` | 10:10 | 36.2 MB | 2026-11-18 |

---

## Bloque Formularios  (id 2)

- **Origen:** Release `Grabaciones` (v1.0). Videos subidos después del Bloque 1.
- **Estado:** abierto.

| Orden | Título en la web | Archivo | Duración | Tamaño | Alta |
|------:|------------------|---------|---------:|-------:|------|
| 1 | Formularios, parte 1 | `Formularios_parte1.mp4` | 45:15 | 162 MB | 2026-11-18 |
| 2 | Formularios, parte 2 | `Formularios_parte2.mp4` | 31:33 | 147 MB | 2026-11-18 |
| 3 | Formularios 3 | `Formularios_3.mp4` | 1:21:03 | 337 MB | 2026-11-18 |
| 4 | Formularios, corrección | `Formularios_correccion.mp4` | 1:31:55 | 417 MB | 2026-11-18 |
| 5 | Extras de formularios | `Extras_formu.mp4` | 22:45 | 77.4 MB | 2026-11-18 |

> Orden propuesto: parte 1, parte 2, 3, corrección y extras. Pendiente de confirmar por Igor.

---

## Bloque 2  (id 3)

- **Origen:** Release `Grabaciones` (v1.0). 16 videos subidos el 2026-11-19 (copias en `webs/video/`).
- **Estado:** abierto.
- **Nombres:** GitHub cambia algunos nombres al subir (espacios por puntos, sin tildes ni paréntesis). En la web va **el nombre de la release**.

| Orden | Título en la web | Archivo (release) | Duración | Tamaño | Alta |
|------:|------------------|-------------------|---------:|-------:|------|
| 1 | Inicio de CSS | `Inicio_CSS.mp4` | 1:03:02 | 234 MB | 2026-11-19 |
| 2 | CSS básico | `Basico_CSS.mp4` (local: `Básico_CSS.mp4`) | 1:26:16 | 345 MB | 2026-11-19 |
| 3 | Ejercicio CSS 2 | `Ejercicio_CSS_2.mp4` | 21:41 | 85 MB | 2026-11-19 |
| 4 | Ejercicio básico 2: CSS anidado, parte 1 | `EjercicioBasico_2_css_anidado_parte_1.mp4` | 51:03 | 205 MB | 2026-11-19 |
| 5 | Ejercicio básico 2: CSS anidado, parte 2 | `EjercicioBasico_2_css_anidado_parte_2.mp4.mp4` | 1:46:45 | 485 MB | 2026-11-19 |
| 6 | Favicon y fuentes, parte 1 | `favicon-fuentes-1.mp4` | 48:19 | 227 MB | 2026-11-19 |
| 7 | Favicon y fuentes, parte 2 | `favicon-fuentes-2.mp4` | 35:49 | 186 MB | 2026-11-19 |
| 8 | Cursores, eventos y efectos | `cursos_eventos_efectos.mp4` | 1:49:46 | 469 MB | 2026-11-19 |
| 9 | Anclas y efectos | `anclas.y.efectos.mp4` (local: `anclas y efectos.mp4`) | 1:17:50 | 409 MB | 2026-11-19 |
| 10 | Backgrounds (parcial) | `Backgrounds.parcial.mp4` (local: `Backgrounds(parcial).mp4`) | 1:54:23 | 547 MB | 2026-11-19 |
| 11 | Popover | `Popover.mp4` | 31:53 | 146 MB | 2026-11-19 |
| 12 | Flexbox, parte 1.1 | `flexbox_Parte_1.1.mp4` | 1:53:42 | 475 MB | 2026-11-19 |
| 13 | Flexbox, parte 1.2 | `flexbox_Parte_1.2.mp4` | 55:48 | 249 MB | 2026-11-19 |
| 14 | Flexbox, parte 2 | `flexbox_Parte_2.mp4` | 1:40:52 | 436 MB | 2026-11-19 |
| 15 | Corrección Flexbox 1 | `Correccion_FlexBox1.mp4` | 45:43 | 180 MB | 2026-11-19 |
| 16 | Ejercicio «Muerte» 1 | `ejercicioMuerte1.mp4` | 1:27:38 | 429 MB | 2026-11-19 |
| 17 | Corrección Pokédex | `correccion_pokedex.mp4` | 50:59 | 257 MB | 2026-11-18 |

> Orden 1-16 confirmado por Igor el 2026-11-19. El 16 (mix-blend-mode, corner-shape y paint-order) va al Bloque 3 por indicación de Igor (2026-11-24), al final. La Corrección Pokédex (venía del Bloque 1) va al final para no mover el orden confirmado.

---

## Bloque 3  (id 4)

- **Origen:** Release `Grabaciones` (v1.0). 15 videos subidos el 2026-11-19 y 1 el 2026-11-24 (copias en `webs/video/`).
- **Estado:** abierto.

| Orden | Título en la web | Archivo (release) | Duración | Tamaño | Alta |
|------:|------------------|-------------------|---------:|-------:|------|
| 1 | Popover y vídeo, parte 1 | `popover.y.video_1.mp4` (local: `popover y video_1.mp4`) | 46:35 | 176 MB | 2026-11-19 |
| 2 | Popover y vídeo, parte 2 | `popover.y.video_2.mp4` (local: `popover y video_2.mp4`) | 44:34 | 218 MB | 2026-11-19 |
| 3 | Vídeo 3: aspect-ratio y object-fit | `popoVideo_3_aspectRatio_object_fit.mp4` | 1:34:57 | 463 MB | 2026-11-19 |
| 4 | Transiciones, parte 1 | `Transition1.mp4` | 1:47:12 | 475 MB | 2026-11-19 |
| 5 | Transform, parte 1 | `Transform1Parte.mp4` | 1:44:03 | 444 MB | 2026-11-19 |
| 6 | Transform, parte 2 | `Transform2Parte.mp4` | 1:32:04 | 439 MB | 2026-11-19 |
| 7 | Panoplia: transiciones 1 | `Panoplia_transition_1.mp4` | 1:40:53 | 384 MB | 2026-11-19 |
| 8 | Panoplia: transiciones 2 | `Panoplia_transition_2.mp4` | 1:09:11 | 291 MB | 2026-11-19 |
| 9 | Panoplia: transiciones 3 | `Panoplia_transition_3.mp4` | 1:46:25 | 579 MB | 2026-11-19 |
| 10 | Panoplia: transiciones 4 | `Panoplia_transition_4.mp4` | 1:02:07 | 289 MB | 2026-11-19 |
| 11 | Panoplia: transiciones 5 | `Panoplia_transition_5.mp4` | 29:39 | 137 MB | 2026-11-19 |
| 12 | Panoplia: transiciones 6 | `Panoplia_transition6.mp4` | 1:43:10 | 519 MB | 2026-11-19 |
| 13 | Instrucciones de recorte | `Intrucciones_recorte.mp4` | 23:58 | 172 MB | 2026-11-19 |
| 14 | Heroes of arroz caldosio | `Heroes_of_arroz_caldosio.mp4` | 1:34:35 | 616 MB | 2026-11-19 |
| 15 | Repaso intenso | `Repaso_intenso.mp4` | 55:33 | 232 MB | 2026-11-19 |
| 16 | Mix-blend-mode, corner-shape y paint-order | `Mix-blend-mode-corner-shape-paint-order.mp4` | 1:21:39 | 322 MB | 2026-11-24 |

> Orden por temas (popover y vídeo, transiciones, transform, proyecto Panoplia, recorte, Heroes y repaso), confirmado por Igor el 2026-11-19. El 16 (mix-blend-mode, corner-shape y paint-order) va al Bloque 3 por indicación de Igor (2026-11-24), al final.

---

## Historial de cambios

| Fecha | Cambio |
|-------|--------|
| 2026-11-18 | Creación del registro. Bloque 1 = videos de Releases/Grabaciones. |
| 2026-11-18 | Bloque 1 completado con 5 videos (v1.0). |
| 2026-11-18 | Título cambiado a "Videoteca Igor teechah" (teechah en cursiva). Añadido `logo.webp`. Nuevo estilo graffiti. |
| 2026-11-18 | Creado "Bloque Formularios" (id 2), separado del Bloque 1. Nombres de sus videos pendientes. |
| 2026-11-18 | Bloque Formularios completado con 5 videos (parte1, parte2, 3, correccion, extras). Total release: 10 videos. |
| 2026-11-18 | Web: bloques desplegables (cerrados al abrir) y videos con carga bajo demanda (solo se descargan al pulsar play). No cambia el contenido de ningún bloque. |
| 2026-11-18 | Web rediseñada: «Igor-Movies» como tele (canales y cintas VHS), reproductor grande con anterior/siguiente y velocidad, continuar por donde ibas, buscador, duraciones, precarga del índice al pasar el ratón. Añadido `faststart.py`. No cambia el contenido de ningún bloque. |
| 2026-11-18 | Los 10 videos pasados por `faststart.py` y vueltos a subir con el mismo nombre (mismo contenido, índice al principio). |
| 2026-11-19 | Creado «Bloque 2» (id 3) con 16 videos, ya pasados por `faststart.py`. Flujo simplificado: Igor sube los videos tal cual y Claude los prepara. |
| 2026-11-19 | Formularios pasa a mostrarse entre el Bloque 1 y el Bloque 2. Corrección Pokédex movida del Bloque 1 al Bloque 2. Creado «Bloque 3» (id 4) con 15 videos, pasados por `faststart.py`. |
| 2026-11-24 | Bloque 3: añadido «Mix-blend-mode, corner-shape y paint-order» (1:21:39), pasado por `faststart.py`. |

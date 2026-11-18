# Registro de videos: Videoteca Igor teechah

Fuente de verdad de qué video pertenece a qué bloque y en qué orden. **Nunca se mezclan videos entre bloques.**
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

1. **Antes de subir**, pasa cada video por `faststart.py` (abajo). Sin este paso, una clase larga tarda más de 10 segundos en empezar.
2. Subes los videos nuevos a la release.
3. Me pasas los nombres de archivo y el bloque al que van (y este `.md`).
4. Yo actualizo este registro y `index.html` (título, archivo y **duración**), sin mover videos de un bloque a otro.

### Por qué tardaban en cargar y cómo se arregla

Un MP4 lleva un **índice** (la caja `moov`: dónde está cada segundo de imagen y sonido). OBS lo escribe **al final** del archivo, porque no sabe cuánto durará la grabación hasta que paras. El navegador necesita ese índice para empezar: con el índice al final tiene que pedir el principio, saltar al final, descargar el índice (hasta 5 MB en las clases de hora y media) y volver. Contra GitHub, cada salto pasa además por una redirección. Medido el 2026-11-18: **11,5 s** para arrancar `Formularios_correccion.mp4`.

La solución es mover el índice al principio («faststart»). No se recomprime nada: la imagen, el sonido y la calidad quedan idénticos, solo cambia el orden de las piezas.

```
python faststart.py original.mp4 listo.mp4
```

El script comprueba él mismo que el resultado está bien. Si tienes ffmpeg, es lo mismo que `ffmpeg -i original.mp4 -c copy -movflags +faststart listo.mp4`.

**Estado de los videos ya subidos (2026-11-18):** los 10 tienen el índice al final. Pendiente: pasarlos por `faststart.py` y volver a subirlos con el mismo nombre (la web no cambia).

Mientras tanto, la web ayuda en dos cosas: se conecta a GitHub nada más abrirse (`preconnect`) y, al pasar el ratón o el foco por una cinta, empieza a descargar su índice. Medido: **0,8 s** de arranque si pasas el ratón un par de segundos antes de pulsar.

---

## Bloque 1  (id 1)

- **Origen:** Release `Grabaciones` (v1.0). Los 5 primeros videos subidos.
- **Estado:** cerrado, salvo que se indique lo contrario.

| Orden | Título en la web | Archivo | Duración | Tamaño | Alta |
|------:|------------------|---------|---------:|-------:|------|
| 1 | Boceto general | `boceto_general.mp4` | 37:30 | 191 MB | 2026-11-18 |
| 2 | Corrección Pokédex | `correccion_pokedex.mp4` | 50:59 | 257 MB | 2026-11-18 |
| 3 | Cuarto ejercicio | `Cuarto.ejercicio.mp4` | 17:52 | 92.3 MB | 2026-11-18 |
| 4 | Popurri | `Popurri.mp4` | 42:35 | 164 MB | 2026-11-18 |
| 5 | Primer ejercicio | `primerEjercicio.mp4` | 10:10 | 36.2 MB | 2026-11-18 |

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

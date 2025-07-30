# 🧭 Influent Package Maker (IPM) – Powered by Influent Studios

## 🧭 Descripción

Este proyecto forma parte del ecosistema de herramientas visuales y de automatización desarrollado por Influent Studios. Está pensado como una plantilla base para scripts en Python, compatible con sistemas como Package Maker e IPM (Influent Package Manager).

A través de un diseño ordenado y altamente comentado, permite a desarrolladores y diseñadores iniciar módulos visuales o lógicos sin preocuparse por la estructura inicial. Ideal para quienes valoran compatibilidad multiplataforma, claridad visual, estilo profesional y expansión modular.

---

## 📁 Generación de estructura y carpetas

El entorno permite la generación automática de carpetas y rutas necesarias para alojar el script, sus estilos y recursos visuales:

- Carpeta principal del proyecto: `self.project_path`
- Carpetas generadas: app, config, docs, assets, lib
- Se copia el icono principal `app\app-icon.ico` y se traslada a un nuevo proyecto
- Se usa `config\` como archivos de configurador y sesiones
- Se usa `docs\` para la documentacion `index.html` en caso de un `Github Pages`
- Se usa `assets` para el manejo de archivos multimedia y `meda-graph`
- Se usa `lib\` para alojar los  `requeriments.txt` de un python o dicha `library` de cualquier lenguaje
- Se usa `app\` como envoltorio principal de la app para no ocupar espacio en disco
- Se usa `mod\` o `engine\` (dependiendo de la `v` que se utilice en dicho entorno), para alojar scripts `giratorios` los cuales cambian el comportameinto de el script y dichas reglas. Lo cual se puede exponer a virus si no se emplea de manera correcta
- Se compila el envoltorio grupal (carpeta de proyecto completa), dentro de la carpeta de Proyectos en su carpeta de Documentos predeterminada por su sistema a un ZIP que puede ser renombrado auto a .ikp (Influent Kompiled Package)
- Se implementa un antivirus en la v3 para evitar virus y malos despliegues dentro del paquete (volatile)
- Se implementa a `Gabo AI` con `prompts` predeterminados seguidos de los que pide el usuario para generar proyectos inteligentemente.
- Ruta de salida para script generado:  
  `assets/<nombre_interno>.v<versión_formateada>.py`
- Validación y creación automática:  
  `os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)`

Esto asegura compatibilidad incluso si el entorno se ejecuta en sistemas sin estructura previa. El creador se encarga de generar carpetas faltantes al copiar `template.py`.

---

## 📣 ¿Para quién es este proyecto?

Este repositorio es ideal si tú:

- ✅ Quieres comenzar módulos visuales o CLI sin código repetitivo
- ✅ Buscas compatibilidad entre sistemas como FlurryOS e IPM
- ✅ Prefieres estructuras comentadas y fáciles de leer
- ✅ Trabajas con edición visual y quieres una base estilizada
- ✅ Necesitas generar scripts automáticamente desde interfaces gráficas

---

## 🧪 Capturas de ejemplo

- Ejecución visual del IPM:

  ![photo1](assets/photo1.png)

- Contenedor de archivos:

  ![photo2](assets/photo2.png)

---

## 🔧 Estructura del script `assets\template.py`

- Importación modular (`sys`, `os`, `PyQt5`)
- Variables de color y nombre integradas
- Interfaz gráfica con `QWidget`, `QPushButton`, `QLabel`
- Separación de funciones (`init_ui`, `accion`)
- Línea especial `#strikemode` como delimitador visual para edición controlada

---

## 💄 Estilos `.pyqss` para diseño visual

El archivo `template.qss` permite aplicar estilos en tiempo real al script:

- `QWidget` con fondo personalizado
- `QPushButton` con hover, padding y bordes redondeados
- `QLabel` con tipografía controlada
- Compatible con previsualizadores IPM

---

## 👤 Sobre el autor – Jesús Quijada

Jesús Quijada es diseñador y desarrollador visual, creador de herramientas como FlurryOS, IPM y Package Maker. Trabaja desde Anzoátegui en conectar visuales dinámicos con estructuras multiplataforma compatibles, usando avatares como Gabo Al para dar narrativa a su ecosistema creativo.

Su estilo se basa en gradientes, estructuras limpias, automatización y una visión clara para expandir visualmente cualquier marca. Integra redes como Instagram y GitHub Pages para mantener una presencia cohesiva y profesional.

---

## 🚧 Qué esperar para la v3

La próxima versión traerá:

- 🧬 Interfaces puramente terminales con emojis y color
- 🧠 Generador visual `.pyqss` desde interfaz IPM
- 🌍 Meta tags automáticos para GitHub Pages y vista social
- 🎬 Splash animado con rutas preconfiguradas desde creator
- 💬 Traducción visual con `QTranslator` desde config avanzada
- 🔁 Presets desde Package Maker y exportación multiplataforma

---

## 🪄 Línea de comando rápida

- Ejecutar desde terminal:

  ```bash
  python3 packagemaker.vX.py```
---

## 📬 Contacto y contribuciones

- Instagram: `@jesusquijada34`
- GitHub: `@jesusquijada34`
- Telegram: `t.me/jesusquijada34`
- Licencia: MIT
- ¿Ideas o mejoras? ¡Envíalas por Pull Request, a `feddbackus.ikp` o a mi correo electronico `jesusquijada.34553902@gmail.com` y se revisan en vivo!

---

## 📑 Changelog reciente

### 🆕 v2.5.2
- Añadido soporte para generación automática de carpetas
- README actualizado con sección de uso estructural
- Inclusión de comandos terminales en sección CLI


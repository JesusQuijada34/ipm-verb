# 🧭 Influent Package Manager (IPM)
### Influent Package Manager (IPM) es un sistema modular de gestión y empaquetado de aplicaciones, diseñado por Jesús Quijada, con el propósito de simplificar y estandarizar el desarrollo de software distribuible, especialmente en entornos Linux como Zorin OS. Más allá de ser un simple empaquetador, IPM es una filosofía de organización creativa y técnica que refleja una preocupación por la estética, la compatibilidad multiplataforma y la autonomía del desarrollador.

# 🛠️ Origen del proyecto
### IPM fue creado como una solución personal para automatizar y estructurar el flujo de trabajo al desarrollar múltiples aplicaciones creativas — como Influent Camera — permitiendo:

### Documentar cada app automáticamente

### Generar paquetes .ifp y .ifb para fácil distribución

### Acompañar cada entrega con su ícono, requerimientos y metadata descriptiva

### Evitar la dependencia de formatos externos como .deb, .rpm o AppImage

### Jesús observó la necesidad de algo más sencillo, visual y personalizable, que pudiera evolucionar hacia un ecosistema completo de herramientas Influent — cada una con su propia identidad y propósito.

# 🧠 Filosofía técnica
> IPM se construye sobre los siguientes principios:

### Legibilidad: El código está cuidadosamente organizado, con variables globales definidas al inicio y menús ANSI que mejoran la experiencia en terminal.

### Modularidad: Cada paquete se aloja en su propia carpeta, con estructura estándar (app, config, docs, assets, lib) para facilitar edición y navegación.

### Automatización inteligente:

### Generación automática de details.xml con metadatos únicos, hash SHA256, fecha y clasificación de edad por palabras clave.

### Generación interactiva o automática de README.md con estructura, requisitos, ejemplos y descripción.

### Compresión con barra de progreso visual usando tqdm.

# 👤 Sobre el creador
### Jesús Quijada es un desarrollador multidisciplinario apasionado por la convergencia entre estética visual y funcionalidad técnica. Con experiencia avanzada en Python, scripting multiplataforma, GUI moderna con CustomTkinter y distribución modular, su enfoque se distingue por:

# Temáticas limpias y vibrantes en el diseño de interfaces

### Iteración constante buscando perfección técnica y visual

### Autonomía creativa para construir herramientas que van más allá del estándar

### IPM es la manifestación tangible de esa mentalidad: una herramienta creada por y para desarrolladores que quieren controlar cada aspecto de su entrega.

# 🧰 Tecnologías utilizadas
> Python 3.10+

> tqdm para barra de progreso

> xml.etree.ElementTree para metadatos

> ANSI para interfaz en terminal

> Formato .ifp y .ifb como estándar personalizado

# 🧪 Estructura típica de un paquete
``` influent.camera.v1/ ├── app/ │ ├── camera.v1.py │ └── app-icon.ico ├── assets/ ├── config/ ├── docs/ ├── lib/ │ └── requirements.txt ├── details.xml └── README.md ```

# 📦 ¿Qué vendrá después?
### IPM es solo el principio de un ecosistema donde cada app puede ser creada, empaquetada, documentada y distribuida con total estilo y control. Jesús planea integrar funciones como:

### Instalador automático de dependencias

### Detector de GUI y CLI para generar lanzadores .desktop

### Exportación directa a USB o Web con firma criptográfica

### Integración con Influent Dashboard para visualizar apps install

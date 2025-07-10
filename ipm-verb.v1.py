import os
import time
import shutil
import hashlib
import zipfile
import xml.etree.ElementTree as ET
from tqdm import tqdm
import subprocess

# 🎨 Colores ANSI
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# 📁 Rutas base
BASE_DIR = os.path.expanduser("~/Documentos/Influent Packages")
DESKTOP = os.path.expanduser("~/Escritorio")
IPM_ICON_PATH = os.path.join(os.path.dirname(__file__), "app", "app-icon.ico")

# 📁 Carpetas predeterminadas
DEFAULT_FOLDERS = "app,assets,banderas,config,docs,ke,lib,source"

# 🧠 Clasificación por edad
AGE_RATINGS = {
    "adult": "Solo Adultos",
    "violence": "18+",
    "kids": "Para niños",
    "teen": "Solo Adolescentes",
    "camera": "Todas las edades",
    "calculator": "Todas las edades",
    "game": "18-",
}

# 🧾 Crear archivo XML de detalles
def create_details_xml(path, empresa, nombre_logico, nombre_completo, version):
    full_name = f"{empresa}.{nombre_logico}.v{version}"
    hash_val = hashlib.sha256(full_name.encode()).hexdigest()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    rating = "Todas las edades"
    for keyword, rate in AGE_RATINGS.items():
        if keyword in nombre_logico.lower() or keyword in nombre_completo.lower():
            rating = rate
            break

    root = ET.Element("app")
    ET.SubElement(root, "empresa").text = empresa
    ET.SubElement(root, "nombre_logico").text = nombre_logico
    ET.SubElement(root, "nombre_completo").text = nombre_completo
    ET.SubElement(root, "version").text = f"v{version}"
    ET.SubElement(root, "creado_en").text = "Zorin OS"
    ET.SubElement(root, "fecha").text = timestamp
    ET.SubElement(root, "hash").text = hash_val
    ET.SubElement(root, "clasificacion").text = rating

    tree = ET.ElementTree(root)
    tree.write(os.path.join(path, "details.xml"))

# 🧱 Comprimir con barra de progreso
def zip_with_progress(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        file_list = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                file_list.append((full_path, arcname))

        for full_path, arcname in tqdm(file_list, desc="📦 Comprimiendo", unit="archivo"):
            zipf.write(full_path, arcname)

# 🏗️ Crear estructura de paquete
def create_package():
    subprocess.run(['clear'])
    print(f">{RED}???.???.???")
    empresa = input(f"{CYAN}Nombre de la empresa: {RESET}").strip().lower().replace(" ", "-")
    subprocess.run(['clear'])
    print(f">{RED}{empresa}.???.???")
    nombre_logico = input(f"{CYAN}Nombre lógico de la app (sin espacios): {RESET}").strip().lower()
    subprocess.run(['clear'])
    print(f">{RED}{empresa}.{nombre_logico}.???")
    version = input(f"{CYAN}Versión (solo número, ej. 1): {RESET}").strip()
    subprocess.run(['clear'])
    print(f">{GREEN}{empresa}.{nombre_logico}.v{version}")
    nombre_completo = input(f"{CYAN}Nombre completo de la app {GREEN}(RECOMENDADO: {nombre_logico}){CYAN}: {RESET}").strip()

    folder_name = f"{empresa}.{nombre_logico}.v{version}"
    full_path = os.path.join(BASE_DIR, folder_name)

    for folder in DEFAULT_FOLDERS.split(","):
        os.makedirs(os.path.join(full_path, folder.strip()), exist_ok=True)

    # Crear archivo principal
    main_script = os.path.join(full_path, f"{nombre_logico}.v{version}.py")
    with open(main_script, "w") as f:
        f.write(f"# {nombre_completo} - v{version}\n# Autor: {empresa}\n\nprint('¡Bienvenido a {nombre_completo}!')\n")

    # Copiar ícono
    icon_dest = os.path.join(full_path, "app", "app-icon.ico")
    try:
        shutil.copy(IPM_ICON_PATH, icon_dest)
    except Exception as e:
        subprocess.run(['clear'])
        print(f"{RED}❌ No se pudo copiar el ícono: {e}{RESET}")

    # Crear requirements.txt
    requirements_path = os.path.join(full_path, "lib", "requirements.txt")
    with open(requirements_path, "w") as f:
        f.write("# Dependencias del paquete\n")
        f.write("customtkinter\nopencv-python\npillow\n")

    # Crear detalles
    create_details_xml(full_path, empresa, nombre_logico, nombre_completo, version)
    subprocess.run(['clear'])
    print(f"{GREEN}✅ Paquete creado en: {full_path}{RESET}")# 📝 Generar README automáticamente
    readme_path = os.path.join(full_path, "README.md")
    readme_text = f"""# {nombre_completo}

Paquete generado con Influent Package Manager.

---

## 📦 Ejemplo de uso

```bash
python3 {empresa}.{nombre_logico}.v{version}/{nombre_logico}.v{version}.py
```

---

## 🧪 Requisitos

```bash
pip install -r lib/requirements.txt
```

---

## 📁 Estructura

```
{folder_name}/
├── app/
│   ├── {nombre_logico}.v{version}.py
│   └── app-icon.ico
├── assets/
├── config/
├── docs/
├── ke/
├── banderas/
├── source/
├── lib/
│   └── requirements.txt
└── details.xml
```

---

## 👤 Autor

{empresa}
"""

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_text)

    print(f"{GREEN}📝 README.md generado automáticamente en: {full_path}{RESET}")

    
# 🔨 Construir paquete .ifp/.ifb
def build_package():
    print(f"{CYAN}🔨 Construcción de paquete .ifp/.ifb{RESET}")
    empresa = input(f"{CYAN}Empresa (formato lógico): {RESET}").strip().lower()
    nombre = input(f"{CYAN}Nombre lógico de la app: {RESET}").strip().lower()
    version = input(f"{CYAN}Versión (solo número): {RESET}").strip()
    tipo = input(f"{YELLOW}¿Tipo de paquete? (1 = .ifp normal, 2 = .ifb ligero): {RESET}").strip()

    folder = f"{empresa}.{nombre}.v{version}"
    path = os.path.join(BASE_DIR, folder)
    if not os.path.exists(path):
        print(f"{RED}❌ No se encontró la carpeta del paquete.{RESET}")
        return

    ext = ".ifp" if tipo == "1" else ".ifb"
    output_file = os.path.join(BASE_DIR, folder + ext)
    zip_path = output_file.replace(ext, "") + ".zip"

    zip_with_progress(path, zip_path)
    os.rename(zip_path, output_file)
    
    subprocess.run(['clear'])
    print(f"{GREEN}✅ Paquete construido: {output_file}{RESET}")
    
# 🚀 Menú principal
def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    while True:
        subprocess.run(['clear'])
        print(f"""{CYAN}
╔══════════════════════════════════════╗
║     {GREEN}INFLUENT PACKAGE MAKER v1{CYAN}        ║
╚══════════════════════════════════════╝{RESET}
{GREEN}[1] Crear nuevo paquete
{YELLOW}[2] Construir paquete (.ifp/.ifb)
{RED}[0] Salir
""")
        option = input(f"{MAGENTA}[>] {RESET}").strip()
        if option == "1":
            create_package()
        elif option == "2":
            build_package()
        elif option == "0":
            subprocess.run(['clear'])
            print(f"{CYAN}¡Hasta luego! 👋{RESET}")
            break
        else:
            subprocess.run(['clear'])
            print(f"{RED}❌ Opción inválida. Intenta de nuevo.{RESET}")

if __name__ == "__main__":
    main()

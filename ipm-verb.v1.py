import os, sys, json, subprocess, pkg_resources
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QLabel, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyle

STYLE_GLOBAL = """
QWidget {
    background-color: #f5f5f5;
    font-family: Arial;
    color: #333;
    border: none;
}

QPushButton {
    background-color: #e0e0e0;
    border: 2px solid #ccc;
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #d6d6d6;
    border: 2px solid #999;
}

QPushButton:pressed {
    background-color: #c0c0c0;
    border: 2px solid #666;
}
"""

def ruta_base():
    if sys.platform.startswith("win"):
        return os.path.join(os.environ["USERPROFILE"], "Documents", "Influent Packages")
    else:
        return os.path.join(os.path.expanduser("~"), "Documentos", "Influent Packages")

def leer_manifest(carpeta):
    path = os.path.join(carpeta, "manifest.json")
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return None

def leer_requirements(carpeta):
    reqs = []
    path = os.path.join(carpeta, "requirements.txt")
    if not os.path.exists(path):
        return reqs
    try:
        with open(path, "r", encoding="utf-8") as f:
            for linea in f:
                limpio = linea.strip()
                if limpio and not limpio.startswith("#"):
                    reqs.append(limpio)
    except:
        pass
    return reqs

def requerimientos_faltantes(lista):
    faltantes = []
    for req in lista:
        try:
            pkg_resources.require([req])
        except:
            faltantes.append(req)
    return faltantes

def instalar_paquetes(paquetes):
    for paquete in paquetes:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])
        except Exception as e:
            mostrar_mensaje("Error al instalar", f"No se pudo instalar: {paquete}", str(e))

def ejecutar_script(path_script):
    if not os.path.exists(path_script):
        mostrar_mensaje("Script no encontrado", f"No existe: {path_script}")
        return
    try:
        subprocess.run([sys.executable, path_script], check=True)
        mostrar_mensaje("Ejecución exitosa", f"El script se ejecutó correctamente:\n{path_script}")
    except subprocess.CalledProcessError as e:
        mostrar_mensaje("Error al ejecutar", f"Falló al ejecutar el script", str(e))

def mostrar_mensaje(titulo, texto, detalles=""):
    app = QApplication.instance() or QApplication(sys.argv)
    mbox = QMessageBox()
    mbox.setWindowTitle(titulo)
    mbox.setText(texto)
    if detalles:
        mbox.setDetailedText(detalles)
    mbox.setStandardButtons(QMessageBox.Ok)
    mbox.exec_()

def mostrar_detalles_manifest(manifest):
    app = QApplication.instance() or QApplication(sys.argv)
    mbox = QMessageBox()
    mbox.setWindowTitle(f"Detalles de: {manifest.get('name', 'Paquete IPM')}")
    
    texto = (
        f"👤 Autor: {manifest.get('author', 'Desconocido')}\n"
        f"📦 Versión: {manifest.get('version', '0.0.1')}\n"
        f"📝 Descripción:\n{manifest.get('description', 'Sin descripción.')}"
    )
    
    mbox.setText(texto)
    detalles = json.dumps(manifest, indent=4, ensure_ascii=False)
    mbox.setDetailedText(detalles)
    
    icono = QApplication.style().standardIcon(QStyle.SP_FileDialogContentsView)
    mbox.setIconPixmap(icono.pixmap(48, 48))
    mbox.setStandardButtons(QMessageBox.Ok)
    mbox.exec_()

def detectar_y_ejecutar():
    base = ruta_base()
    carpetas = [f for f in os.listdir(base) if os.path.isdir(os.path.join(base, f))]
    for nombre in carpetas:
        ruta = os.path.join(base, nombre)
        manifest = leer_manifest(ruta)
        if manifest and "main" in manifest:
            reqs = leer_requirements(ruta)
            faltan = requerimientos_faltantes(reqs)
            if faltan:
                instalar_paquetes(faltan)
            mostrar_detalles_manifest(manifest)
            script = os.path.join(ruta, manifest["main"])
            ejecutar_script(script)
            return
    mostrar_mensaje("No ejecutado", "No se encontró ningún paquete IPM válido con 'main'.")

class IPMWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(400, 300)
        self.setStyleSheet(STYLE_GLOBAL)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("🚀 Lanzador IPM")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.btn_verificar = QPushButton("Verificar & Ejecutar")
        self.btn_verificar.clicked.connect(self.iniciar_verificacion)
        layout.addWidget(self.btn_verificar)

        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.close)
        layout.addWidget(self.btn_salir)

        self.setLayout(layout)

    def iniciar_verificacion(self):
        detectar_y_ejecutar()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = IPMWindow()
    ventana.show()
    sys.exit(app.exec_())
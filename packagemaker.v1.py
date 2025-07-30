#!/usr/bin/env python
import os, sys, argparse, platform, datetime
from colorama import init, Fore, Style

init(autoreset=True)

def sistema_emoji():
    sistema = platform.system()
    return {
        "Windows": "🪟",
        "Linux": "🐧",
        "Darwin": "🍎",
        "Android": "🤖"
    }.get(sistema, "💻")

def color_echo(msg, tipo="info"):
    colores = {
        "info": Fore.BLUE,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "warn": Fore.YELLOW
    }
    emoji = {
        "info": "ℹ️",
        "success": "✅",
        "error": "❌",
        "warn": "⚠️"
    }
    print(f"{colores[tipo]}{emoji[tipo]} {msg}{Style.RESET_ALL}")

def crear_proyecto(empresa, nombre, version):
    path = f"./{empresa}_{nombre}_{version}"
    os.makedirs(path, exist_ok=True)
    color_echo(f"Proyecto creado: {path}", "success")

def compilar_proyecto(empresa, nombre, version):
    sistema = platform.system()
    color_echo(f"Compilando {empresa}/{nombre}/{version} para {sistema}", "info")
    # Simulación de compilación
    color_echo("Compilación completada", "success")

def eliminar_proyecto(empresa, nombre, version):
    path = f"./{empresa}_{nombre}_{version}"
    try:
        os.system(f'rmdir /s /q "{path}"' if os.name == 'nt' else f'rm -rf "{path}"')
        color_echo(f"Proyecto eliminado: {path}", "success")
    except Exception as e:
        color_echo(str(e), "error")

def ejecutar_packagemaker():
    if os.path.exists("packagemaker.v1.py"):
        os.system(f"{sys.executable} packagemaker.v1.py")
        color_echo("Packagemaker ejecutado", "success")
    else:
        color_echo("No se encontró packagemaker.v1.py", "error")

def main():
    parser = argparse.ArgumentParser(description="💻 IPM Terminal Edition - Modo compacto multiplataforma")
    parser.add_argument('--create', nargs=3, metavar=('EMPRESA', 'NOMBRE', 'VERSION'))
    parser.add_argument('--add', nargs=3, metavar=('EMPRESA', 'NOMBRE', 'VERSION'))
    parser.add_argument('--remove', nargs=3, metavar=('EMPRESA', 'NOMBRE', 'VERSION'))
    parser.add_argument('--init', action='store_true')
    parser.add_argument('--helpme', action='store_true')

    args = parser.parse_args()
    emoji_os = sistema_emoji()

    if args.helpme:
        print(Fore.CYAN + f"""
{emoji_os} IPM Terminal Edition
--create "empresa" "nombre" "version"      → Crea estructura de proyecto
--add "empresa" "nombre" "version"         → Compila para sistema activo
--remove "empresa" "nombre" "version"      → Elimina carpeta de proyecto
--init                                     → Ejecuta packagemaker.v1.py
--helpme                                   → Muestra esta ayuda
""" + Style.RESET_ALL)

    elif args.create:
        empresa, nombre, version = args.create
        if version.isdigit() and len(version) == 6:
            version = datetime.datetime.strptime(version, "%y%m%d").strftime("%Y.%m.%d")
        crear_proyecto(empresa, nombre, version)

    elif args.add:
        empresa, nombre, version = args.add
        compilar_proyecto(empresa, nombre, version)

    elif args.remove:
        empresa, nombre, version = args.remove
        eliminar_proyecto(empresa, nombre, version)

    elif args.init:
        ejecutar_packagemaker()
    else:
        color_echo("Ningún parámetro reconocido. Usa --helpme", "warn")

if __name__ == "__main__":
    main()

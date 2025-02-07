import json
import os


def cargar_json(archivo) -> dict:
    """Carga datos desde un archivo JSON."""
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def guardar_json(archivo, datos):
    """Guarda datos en un archivo JSON."""
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)
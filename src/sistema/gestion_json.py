import json
import os

data_path = "data/empleados.json"

def cargar_json() -> dict:
    """Carga datos desde un archivo JSON."""
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def guardar_json(datos: dict):
    """Guarda datos en un archivo JSON."""
    with open(data_path, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)

        
def asegurar_directorio(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
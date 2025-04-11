import json
import os

data_path = "data/empleados.json"

def cargar_json() -> dict:
    """
    Carga datos desde un archivo JSON.

    Esta función lee el archivo `empleados.json` desde la ruta especificada en `data_path`.
    Si el archivo existe, carga los datos JSON en un diccionario y los retorna. Si el archivo no
    existe, retorna un diccionario vacío.

    Retorna:
    --------
    dict
        Diccionario con los datos cargados del archivo JSON, o un diccionario vacío si el archivo no existe.

    Ejemplo de uso:
    ---------------
    datos = cargar_json()
    """
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def guardar_json(datos: dict):
    """
    Guarda datos en un archivo JSON.

    Esta función toma un diccionario `datos` y lo guarda en el archivo `empleados.json` en la ruta especificada en `data_path`.
    Si el archivo no existe, se crea. Los datos son guardados con indentación para mejorar la legibilidad.

    Parámetros:
    -----------
    datos : dict
        Diccionario con los datos a guardar en el archivo JSON.

    Ejemplo de uso:
    ---------------
    datos = {"empleado1": {"nombre": "Juan", "xp": 100}}
    guardar_json(datos)
    """
    with open(data_path, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)

        
def asegurar_directorio(ruta):
    """
    Asegura que un directorio exista.

    Esta función verifica si el directorio especificado por `ruta` existe. Si no existe, crea el directorio
    y todos los directorios intermedios necesarios.

    Parámetros:
    -----------
    ruta : str
        Ruta del directorio que se quiere verificar o crear.

    Ejemplo de uso:
    ---------------
    asegurar_directorio("data/empleados")
    """
    if not os.path.exists(ruta):
        os.makedirs(ruta)
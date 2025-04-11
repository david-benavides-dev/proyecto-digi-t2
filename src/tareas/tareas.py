from sistema.gestion_json import cargar_json, guardar_json


ARCHIVO_TAREAS = "data/nombre_empleado/tareas.json"


# Auxiliar para cargar el JSON de tareas (DEBERIA CARGARSE SIEMPRE AL INICIAR EL PROGRAMA)
def obtener_tareas():
    """
    Carga y retorna las tareas desde el archivo JSON.
    
    Retorna:
        dict: Tareas cargadas del archivo o un diccionario vacío si no existen.
    """
    return cargar_json(ARCHIVO_TAREAS)


def agregar_tarea(nombre, descripcion, xp):
    """
    Agrega una nueva tarea al archivo JSON de tareas.
    
    Parámetros:
        nombre (str): Nombre de la tarea.
        descripcion (str): Descripción de la tarea.
        xp (int): Recompensa en XP.
    """
    tareas = obtener_tareas()
    tareas[nombre] = {"descripcion": descripcion, "xp_gain": xp, "estado": "pendiente"}
    guardar_json(ARCHIVO_TAREAS, tareas)


def completar_tarea(nombre):
    """
    Marca una tarea como completada en el archivo JSON.
    
    Parámetros:
        nombre (str): Nombre de la tarea a completar.
    """
    tareas = obtener_tareas()
    if nombre in tareas and tareas[nombre]["estado"] == "pendiente":
        tareas[nombre]["estado"] = "completada"
        guardar_json(ARCHIVO_TAREAS, tareas)


def mostrar_tareas():
    """
    Muestra todas las tareas con su estado y recompensa en XP.
    """
    tareas = obtener_tareas()
    for nombre, datos in tareas.items():
        print(f"📌 {nombre} ({datos['estado']}) - Recompensa de XP: {datos['xp_gain']}")
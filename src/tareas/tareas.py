from src.sistema.gestion_json import cargar_json, guardar_json


ARCHIVO_TAREAS = "data/nombre_empleado/tareas.json"


# Auxiliar para cargar el JSON de tareas (DEBERIA CARGARSE SIEMPRE AL INICIAR EL PROGRAMA)
def obtener_tareas():
    return cargar_json(ARCHIVO_TAREAS)


def agregar_tarea(nombre, descripcion, xp):
    tareas = obtener_tareas()
    tareas[nombre] = {"descripcion": descripcion, "xp_gain": xp, "estado": "pendiente"}
    guardar_json(ARCHIVO_TAREAS, tareas)


def completar_tarea(nombre):
    tareas = obtener_tareas()
    if nombre in tareas and tareas[nombre]["estado"] == "pendiente":
        tareas[nombre]["estado"] = "completada"
        guardar_json(ARCHIVO_TAREAS, tareas)


def mostrar_tareas():
    tareas = obtener_tareas()
    for nombre, datos in tareas.items():
        print(f"📌 {nombre} ({datos['estado']}) - Recompensa de XP: {datos['xp_gain']}")
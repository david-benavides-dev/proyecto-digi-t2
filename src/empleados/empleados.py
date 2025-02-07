from src.sistema.gestion_json import cargar_json, guardar_json


ARCHIVO_EMPLEADOS = "data/empleados.json"


def obtener_empleados():
    return cargar_json(ARCHIVO_EMPLEADOS)


def agregar_empleado(nombre) -> True:
    empleados = obtener_empleados()
    if nombre not in empleados:
        empleados[nombre] = {"xp": 0}
        guardar_json(ARCHIVO_EMPLEADOS, empleados)
        return True
    else:
        print("Ya existe ese empleado.")
        return False


def agregar_xp(nombre, xp) -> bool:
    empleados = obtener_empleados()
    if nombre in empleados:
        empleados[nombre]["xp"] += xp
        guardar_json(ARCHIVO_EMPLEADOS, empleados)
        return True
    else:
        print("Ese empleado no existe.")
        return False


def mostrar_empleados() -> None:
    empleados = obtener_empleados()
    for nombre, datos in empleados.items():
        print(f"👤 {nombre} - XP: {datos['xp']}")
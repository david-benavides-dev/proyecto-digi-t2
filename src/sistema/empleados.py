from src.sistema.gestion_json import cargar_json, guardar_json


ARCHIVO_EMPLEADOS = "data/empleados.json"


def obtener_empleados():
    return cargar_json(ARCHIVO_EMPLEADOS)


def agregar_empleado(id) -> True:
    empleados = obtener_empleados()
    if id not in empleados:
        empleados[id] = {"xp": 0}
        empleados[id] = {1}
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


def mostrar_info_empleado(empleados: dict, empleado_id: str):
    empleado = empleados.get(empleado_id)
    
    if empleado:
        print(f"Cargando tareas con ID {empleado_id} de {empleado['dni']}")
        print("\n\t\t-*****************************-")
        print("\t\tMisiones principales:")
        
        for tarea in empleado['tareas']:
            if tarea['tipo'] == 'principal':
                estado = "[✓]" if tarea['completada'] else "[X]"
                print(f"\t\t\t{tarea['experiencia_a_dar']}XP {estado} {tarea['descripcion']}")
        
        print("\t\tMisiones opcionales:")
        
        for tarea in empleado['tareas']:
            if tarea['tipo'] == 'opcional':
                estado = "[✓]" if tarea['completada'] else "[X]"
                print(f"\t\t\t{tarea['experiencia_a_dar']}XP {estado} {tarea['descripcion']}")
        
        print("\t\t-*****************************-")
    else:
        print(f"No se encontró información para el empleado con ID {empleado_id}.")


def anadir_tarea_empleado(id_empleado, id_tarea, descripcion, experiencia_a_dar):
    nueva_tarea = {
        "id": id_tarea,
        "descripcion": descripcion,
        "experiencia_a_dar": experiencia_a_dar
    }
    id_empleado['tareas'].append(nueva_tarea)
from sistema.gestion_json import asegurar_directorio
import json
import os

data_path = "data/empleados"

def agregar_empleado():
    """
    Agrega un nuevo empleado al sistema.

    Esta función solicita al usuario el ID y el nombre del empleado, y crea una carpeta para el empleado en la ruta
    especificada en `data_path`. Luego, guarda la información del empleado en un archivo JSON dentro de la carpeta
    del empleado. El empleado es inicializado con 0 puntos de experiencia (XP).

    Ejemplo de uso:
    ---------------
    agregar_empleado()
    """
    worker_id = input("Introduce el ID del nuevo empleado: ")
    nombre = input("Introduce el nombre del empleado: ")
    empleado_dir = os.path.join(data_path, worker_id)
    asegurar_directorio(empleado_dir)
    datos_empleado = {"worker_id": worker_id, "nombre": nombre, "xp": 0}
    with open(os.path.join(empleado_dir, "info.json"), "w", encoding="utf-8") as file:
        json.dump(datos_empleado, file, indent=4, ensure_ascii=False)
    print(f"Empleado {nombre} agregado correctamente.")


def crear_grupo_tareas():
    """
    Crea un grupo de misiones para un empleado.

    Esta función solicita al usuario el ID de un empleado, verifica si el empleado existe, y luego permite
    al usuario crear un nuevo grupo de misiones. El grupo de misiones tiene misiones principales y secundarias
    que el usuario puede definir con una descripción y puntos de experiencia (XP). El grupo de misiones es guardado
    en un archivo JSON dentro de la carpeta del empleado.

    Ejemplo de uso:
    ---------------
    crear_grupo_tareas()
    """
    worker_id = input("Introduce el ID del empleado: ")
    empleado_dir = os.path.join(data_path, worker_id)
    if not os.path.exists(empleado_dir):
        print("Empleado no encontrado.")
        return
    grupo_id = input("Introduce un ID para el grupo de misiones: ")
    archivo_tareas = os.path.join(empleado_dir, f"{grupo_id}.json")
    if os.path.exists(archivo_tareas):
        print("Ya existe un grupo de misiones con esa ID.")
        return
    num_principales = int(input("¿Cuántas misiones principales desea agregar?: "))
    num_secundarias = int(input("¿Cuántas misiones secundarias desea agregar?: "))
    tareas = {"principales": {}, "secundarias": {}}
    for i in range(num_principales):
        tarea_id = f"TID{i+1}"
        descripcion = input(f"Descripción de la misión principal {i+1}: ")
        xp = int(input(f"XP para la tarea principal {i+1}: "))
        tareas["principales"][tarea_id] = {"descripcion": descripcion, "xp": xp, "completado": False}
    for i in range(num_secundarias):
        tarea_id = f"TID{num_principales+i+1}"
        descripcion = input(f"Descripción de la misión secundaria {i+1}: ")
        xp = int(input(f"XP para la misión secundaria {i+1}: "))
        tareas["secundarias"][tarea_id] = {"descripcion": descripcion, "xp": xp, "completado": False}
    with open(archivo_tareas, "w", encoding="utf-8") as file:
        json.dump(tareas, file, indent=4, ensure_ascii=False)
    print("Grupo de misiones creado correctamente.")


def gestionar_tareas():
    """
    Gestiona las misiones de un empleado.

    Esta función permite al jefe gestionar las misiones de un empleado. Solicita el ID del empleado y, si el empleado
    existe, presenta los grupos de misiones asignados. Luego, el jefe puede marcar misiones como completadas y
    asignar puntos de experiencia (XP) al empleado. También puede eliminar misiones completadas del grupo.

    Ejemplo de uso:
    ---------------
    gestionar_tareas()
    """
    worker_id = input("Introduce el ID del empleado: ")
    empleado_dir = os.path.join(data_path, worker_id)
    if not os.path.exists(empleado_dir):
        print("Empleado no encontrado.")
        return
    with open(os.path.join(empleado_dir, "info.json"), "r", encoding="utf-8") as file:
        datos_empleado = json.load(file)
    nombre = datos_empleado["nombre"]
    print(f"MISIONES DE {nombre} - ID {worker_id}")
    print("-*****************************-")
    archivos_tareas = [f for f in os.listdir(empleado_dir) if f.endswith(".json") and f != "info.json"]
    if not archivos_tareas:
        print("No hay grupos de misiones disponibles.")
        return
    for archivo in archivos_tareas:
        print(f"  {archivo[:-5]}")
    grupo_id = input("Introduce la ID del grupo de misiones: ")
    archivo_tareas = os.path.join(empleado_dir, f"{grupo_id}.json")
    if not os.path.exists(archivo_tareas):
        print("Grupo de misiones no encontrado.")
        return
    with open(archivo_tareas, "r", encoding="utf-8") as file:
        tareas = json.load(file)
    print("Misiones principales:")
    for tid, tarea in tareas["principales"].items():
        print(f"  {tid}: {tarea['descripcion']} - {'[✓]' if tarea['completado'] else '[X]'} - {tarea['xp']}XP")
    print("Misiones secundarias:")
    for tid, tarea in tareas["secundarias"].items():
        print(f"  {tid}: {tarea['descripcion']} - {'[✓]' if tarea['completado'] else '[X]'} - {tarea['xp']}XP")
    tarea_id = "TID" + input("Introduce la ID de la misión a validar: ")
    for tipo in ["principales", "secundarias"]:
        if tarea_id in tareas[tipo]:
            tareas[tipo][tarea_id]["completado"] = True
            xp_ganado = tareas[tipo][tarea_id]["xp"]
            datos_empleado["xp"] += xp_ganado
            with open(os.path.join(empleado_dir, "info.json"), "w", encoding="utf-8") as file:
                json.dump(datos_empleado, file, indent=4, ensure_ascii=False)
            print(f"{nombre} ha conseguido {xp_ganado} puntos de experiencia. Actualmente tiene {datos_empleado['xp']}.")
            borrar = input("¿Desea borrar la misión completada? (S/N): ").strip().upper()
            if borrar == "S":
                del tareas[tipo][tarea_id]
                print("Misión eliminada correctamente.")
            break
    with open(archivo_tareas, "w", encoding="utf-8") as file:
        json.dump(tareas, file, indent=4, ensure_ascii=False)
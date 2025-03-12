import os
import json
from src.interfaz.consola import mostrar_menu_empleados
from src.utils.utils import *

data_path = "data/empleados"

def empleado_menu():
    salir = False
    worker_id = input("Introduce tu ID de empleado: ")
    empleado_dir = os.path.join(data_path, worker_id)
    info_path = os.path.join(empleado_dir, "info.json")
    
    if not os.path.exists(info_path):
        print("Empleado no encontrado.")
        return
    
    with open(info_path, "r", encoding="utf-8") as file:
        datos_empleado = json.load(file)
    
    nombre = datos_empleado["nombre"]
    xp = datos_empleado["xp"]
    
    while not salir:
        mostrar_menu_empleados(nombre, xp)
        opcion = pedir_numero("Selecciona una opción: ")
        
        if opcion == 1:
            ver_misiones(worker_id)
        elif opcion == 2:
            completar_misiones(worker_id)
            with open(info_path, "r", encoding="utf-8") as file:
                datos_empleado = json.load(file)
            xp = datos_empleado["xp"]
        elif opcion == 3:
            canjear_xp(worker_id)
        elif opcion == 4:
            print("Saliendo...")
            salir = True
        else:
            print("Opción no válida.")

def ver_misiones(worker_id):
    empleado_dir = os.path.join(data_path, worker_id)
    archivos_tareas = [f for f in os.listdir(empleado_dir) if f.endswith(".json") and f != "info.json"]
    
    if not archivos_tareas:
        print("No hay grupos de misiones disponibles.")
        return
    
    for archivo in archivos_tareas:
        print(f"Grupo de misiones: {archivo[:-5]}")
        with open(os.path.join(empleado_dir, archivo), "r", encoding="utf-8") as file:
            tareas = json.load(file)
        
        print("Misiones principales:")
        for tid, tarea in tareas["principales"].items():
            print(f"  {tid}: {tarea['descripcion']} - {'[✓]' if tarea['completado'] else '[X]'} - {tarea['xp']}XP")
        print("Misiones secundarias:")
        for tid, tarea in tareas["secundarias"].items():
            print(f"  {tid}: {tarea['descripcion']} - {'[✓]' if tarea['completado'] else '[X]'} - {tarea['xp']}XP")
        input("Presione una tecla para continuar...")

def completar_misiones(worker_id):
    empleado_dir = os.path.join(data_path, worker_id)
    info_path = os.path.join(empleado_dir, "info.json")
    
    if not os.path.exists(info_path):
        print("Empleado no encontrado.")
        return
    
    archivos_tareas = [f for f in os.listdir(empleado_dir) if f.endswith(".json") and f != "info.json"]
    if not archivos_tareas:
        print("No hay grupos de misiones disponibles.")
        return
    
    print("Grupos de misiones disponibles:")
    for archivo in archivos_tareas:
        print(f"  {archivo[:-5]}")
    
    grupo_id = input("Introduce el ID del grupo de misiones que deseas completar: ")
    archivo_tareas = os.path.join(empleado_dir, f"{grupo_id}.json")
    
    if not os.path.exists(archivo_tareas):
        print("Grupo de misiones no encontrado.")
        return
    
    with open(info_path, "r", encoding="utf-8") as file:
        datos_empleado = json.load(file)
    
    with open(archivo_tareas, "r", encoding="utf-8") as file:
        tareas = json.load(file)
    

    for tipo in ["principales", "secundarias"]:
        for tid in list(tareas[tipo].keys()):
            if not tareas[tipo][tid]["completado"]:
                tareas[tipo][tid]["completado"] = True
    
    with open(archivo_tareas, "w", encoding="utf-8") as file:
        json.dump(tareas, file, indent=4, ensure_ascii=False)
    

    with open(info_path, "w", encoding="utf-8") as file:
        json.dump(datos_empleado, file, indent=4, ensure_ascii=False)
    
    print(f"Has marcado como completado todas las misiones del grupo {grupo_id}.")

def canjear_xp(worker_id):
    empleado_dir = os.path.join(data_path, worker_id)
    info_path = os.path.join(empleado_dir, "info.json")
    
    if not os.path.exists(info_path):
        print("Empleado no encontrado.")
        return
    
    with open(info_path, "r", encoding="utf-8") as file:
        datos_empleado = json.load(file)
    
    tienda = {"Día libre": 100, "Cena": 200, "Viaje": 500}
    print("Recompensas disponibles:")
    for item, costo in tienda.items():
        print(f"  {item}: {costo} XP")
    
    eleccion = input("¿Qué deseas canjear? (o escribe 'salir' para volver): ")
    if eleccion.lower() == "salir":
        return
    
    if eleccion in tienda and datos_empleado["xp"] >= tienda[eleccion]:
        datos_empleado["xp"] -= tienda[eleccion]
        with open(info_path, "w", encoding="utf-8") as file:
            json.dump(datos_empleado, file, indent=4, ensure_ascii=False)
        print(f"Has canjeado {eleccion}. XP restante: {datos_empleado['xp']}")
    else:
        print("No tienes suficiente XP o la opción no es válida.")

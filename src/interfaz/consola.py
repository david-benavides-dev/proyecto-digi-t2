from src.utils.utils import *


def mostrar_menu_principal(logo: str):
    """
    Muestra el menu principal de la aplicación.
    """
    limpiar_consola()
    print(f"""{logo}
          
     ╔═══════════════════════════════════════╗
     ║  1. Login para jefes                  ║
     ║  2. Login para empleados              ║
     ║  3. Salir                             ║
     ╚═══════════════════════════════════════╝
    """)


def mostrar_menu_master(nombre: str):
    """
    Muestra el menú de los jefes.
    """
    limpiar_consola()
    print(f"""
    ╔═══════════════════════════════════════╗
    ║              Hola {nombre}                ║
    ╠═══════════════════════════════════════╣
    ║  1. Crear un grupo de tareas          ║
    ║  2. Gestionar tareas de un empleado   ║
    ║  3. Agregar nuevo empleado            ║
    ║  4. Salir                             ║
    ╚═══════════════════════════════════════╝
    """)


def mostrar_menu_empleados(nombre: str, xp: int):
    """
    Muestra el menu de los empleados.
    """
    limpiar_consola()
    print(f"""
     ╔═══════════════════════════════════════╗
     ║          Hola {nombre} - XP: {xp}     ║
     ╠═══════════════════════════════════════╣
     ║  1. Comprobar tareas                  ║
     ║  2. Marcar tareas                     ║
     ║  3. Visitar la tienda de puntos       ║
     ║  4. Salir                             ║
     ╚═══════════════════════════════════════╝
    """)


def mensaje_carga_datos():
    print("Comprobando datos...")
    pausar_programa(2)
    print("Datos correctos...")
    pausar_programa(2)
    print("Accediendo...")
    pausar_programa(3)
    limpiar_consola()
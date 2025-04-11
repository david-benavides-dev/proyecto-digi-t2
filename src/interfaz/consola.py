from utils.utils import *


def mostrar_menu_principal(logo: str):
    """
    Muestra el menú principal de la aplicación.

    Este menú incluye opciones para que los usuarios inicien sesión como jefes,
    empleados o salgan de la aplicación.

    Parámetros:
    -----------
    logo : str
        Logo que se muestra en la parte superior del menú principal.
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

    Este menú presenta varias funcionalidades que solo pueden ser accedidas por
    los jefes, tales como la creación de grupos de tareas y la gestión de empleados.

    Parámetros:
    -----------
    nombre : str
        Nombre del jefe que se muestra en el menú.
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
    Muestra el menú de los empleados.

    Este menú permite a los empleados comprobar tareas, marcarlas como completadas
    o visitar la tienda de puntos.

    Parámetros:
    -----------
    nombre : str
        Nombre del empleado que se muestra en el menú.
    xp : int
        Experiencia del empleado que se muestra en el menú.
    """
    #limpiar_consola()
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
    """
    Simula el proceso de carga de datos, mostrando una serie de mensajes en consola
    con pausas entre cada uno para simular la comprobación y acceso a datos.

    Descripción:
    ------------
    Se muestran los siguientes mensajes con pausas simuladas:
      - "Comprobando datos..."
      - "Datos correctos..."
      - "Accediendo..."
    Cada mensaje tiene una pausa de duración específica (pausar_programa(2) o pausar_programa(3)).
    Al final, se limpia la consola.
    """
    print("Comprobando datos...")
    pausar_programa(2)
    print("Datos correctos...")
    pausar_programa(2)
    print("Accediendo...")
    pausar_programa(3)
    limpiar_consola()
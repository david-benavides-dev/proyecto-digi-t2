from src.utils.utils import limpiar_consola


def mostrar_menu_principal(logo: str):
    '''
    Muestra el menu principal de la aplicación.
    '''
    limpiar_consola()
    print(f"""{logo}
          
     ╔═══════════════════════════════════════╗
     ║  1. Login para jefes                  ║
     ║  2. Login para empleados              ║
     ║  3. Salir                             ║
     ╚═══════════════════════════════════════╝
    """)


def mostrar_menu_master(nombre: str):
    limpiar_consola()
    print(f"""
     ╔═══════════════════════════════════════╗
     ║              Hola {nombre}                ║
     ╠═══════════════════════════════════════╣
     ║  1. Crear tareas nuevas (fecha de hoy)║
     ║  2. Modificar tareas existentes       ║
     ║  3. Gestionar tareas de un empleado   ║
     ║  4. Agregar nuevo empleado            ║
     ║  5. Salir                             ║
     ╚═══════════════════════════════════════╝
    """)


def mostrar_menu_empleados(nombre: str, xp: int, seccion_menu: int = 0):
    '''
    Muestra el menu de los empleados.
    '''
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

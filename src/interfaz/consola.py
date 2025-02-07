from src.utils.utils import limpiar_consola


def mostrar_menu_principal(logo: str):
    '''
    Muestra el menu principal de la aplicación.
    '''
    print(f"""{logo}
          
    ********************************************
    *              MENÚ PRINCIPAL              *
    ********************************************
    * 1. Login Empleado                        *
    * 2. Login jefe                            *
    * 3. Salir                                 *
    ********************************************
    """)


def mostrar_menu_empleados():
    '''
    Muestra el menu de los empleados.
    '''
    print("""
    ********************************************
    *              MENÚ PRINCIPAL              *
    ********************************************
    * 1. Login Empleado                        *
    * 2. Login jefe                            *
    * 3. Salir                                 *
    ********************************************

    Por favor, selecciona una opción (1-3):
    """)

# TODO
def mostrar_menu_master(nombre: str, seccion_menu: int = 0):
    limpiar_consola()
    match seccion_menu:
        case 1:
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
        case 2:
            """
            1. Crear tareas nuevas (con fecha de hoy)
            2. Modificar tareas existentes
            3. Gestionar tareas de un empleado
            4. Agregar nuevo empleado
            5. Salir
            """

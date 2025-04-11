from interfaz.consola import *
from interfaz.interface_strings import *
from menus.menu_jefe import *
from sistema.empleados import empleado_menu
from utils.utils import *


def main_menu():
    """
    Muestra el menú principal de la aplicación y permite al usuario elegir entre acceder al menú de jefes, al menú de empleados o salir.

    El flujo de la función es el siguiente:
    1. Muestra el menú principal con las opciones disponibles.
    2. Según la opción seleccionada, ejecuta una de las siguientes acciones:
       - Opción 1: Acceder al menú del jefe.
       - Opción 2: Acceder al menú del empleado.
       - Opción 3: Salir de la aplicación.
    3. Si se selecciona una opción inválida, muestra un mensaje de error y vuelve a mostrar el menú.

    Descripción del flujo:
    -----------------------
    La función entra en un bucle donde el menú principal se muestra repetidamente hasta que el usuario selecciona la opción de salida (opción 3).
    Dependiendo de la opción seleccionada, se ejecutan las funciones:
    - **jefe_menu()**: Muestra el menú para el jefe y permite gestionar tareas relacionadas con los jefes.
    - **empleado_menu()**: Muestra el menú para el empleado y permite gestionar tareas relacionadas con los empleados.
    """
    salir = False

    while not salir:
        mostrar_menu_principal(LOGO)
        opcion = pedir_numero(STRING_GLOBAL_OPCION)
        pausar_programa(1)
        if opcion == 3:
            print(STRING_EXIT)
            salir = True
        else:
            if opcion == 1:
                jefe_menu()
            elif opcion == 2:
                empleado_menu()
                pausar_programa(3)
            else:
                print("Opción no válida")
                pausar_programa(3)
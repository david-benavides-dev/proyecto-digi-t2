from interfaz.consola import *
from interfaz.interface_strings import *
from sistema.jefes import crear_grupo_tareas, agregar_empleado, gestionar_tareas
from utils.utils import *

def jefe_menu():
    """
    Muestra el menú de opciones para el jefe y permite realizar diversas acciones relacionadas con la gestión de tareas y empleados.

    El flujo de la función es el siguiente:
    1. Solicita al jefe su nombre.
    2. Muestra el menú principal con las opciones disponibles para el jefe.
    3. Dependiendo de la opción seleccionada, se ejecutan las siguientes acciones:
       - Opción 1: Crear un grupo de tareas.
       - Opción 2: Gestionar tareas de un empleado.
       - Opción 3: Agregar un nuevo empleado.
       - Opción 4: Salir de la aplicación.
    4. Si el jefe selecciona una opción inválida, se muestra un mensaje de error y se vuelve a mostrar el menú.

    Descripción del flujo:
    -----------------------
    La función solicita al jefe su nombre, luego entra en un bucle en el que se muestra el menú de opciones repetidamente hasta que se elige la opción de salida (opción 4).
    Dependiendo de la opción seleccionada, se ejecutan las funciones correspondientes:
    - **crear_grupo_tareas()**: Permite al jefe crear un grupo de tareas.
    - **gestionar_tareas()**: Permite al jefe gestionar tareas de un empleado.
    - **agregar_empleado()**: Permite al jefe agregar un nuevo empleado.
    """
    salir = False

    nombre = input(STRING_ASK_NAME)
    pausar_programa(1)

    while not salir:
        mostrar_menu_master(nombre)
        opcion = pedir_numero(STRING_GLOBAL_OPCION)
        if opcion == 4:
            print(STRING_EXIT)
            salir = True
        else:
            if opcion == 1:
                print(MENU_2_JEFE_1)
                crear_grupo_tareas()
                pausar_programa(3)
            elif opcion == 2:
                print(MENU_2_JEFE_1)
                mensaje_carga_datos()
                gestionar_tareas()
                pausar_programa(3)
            elif opcion == 3:
                print(MENU_2_JEFE_1)
                agregar_empleado()
                pausar_programa(3)
            else:
                print("Opción no válida")
                pausar_programa(3)
from src.interfaz.consola import *
from src.interfaz.interface_strings import *
from src.sistema.jefes import crear_grupo_tareas, agregar_empleado, gestionar_tareas
from src.utils.utils import *

def jefe_menu():
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
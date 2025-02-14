from src.interfaz.consola import *
from src.interfaz.interface_strings import *


def jefe_menu():
    salir = False

    while not salir:
        nombre = input(STRING_ASK_NAME)
        pausar_programa(1)
        mostrar_menu_master(nombre)
        opcion = pedir_numero(STRING_GLOBAL_OPCION)
        if opcion == 5:
            print(STRING_EXIT)
            salir = True
        else:
            if opcion == 1:
                print(MENU_2_JEFE_1)
                nombre_empleado = input(MENU_2_JEFE_2)
                mensaje_carga_datos()
                salir = True
            elif opcion == 2:
                mostrar_menu_empleados()
                pausar_programa(3)
            elif opcion == 3:
                nombre_empleado = input(MENU_1_JEFE_1)
                dni = pedir_numero(MENU_1_JEFE_2)
                mensaje_carga_datos()
                salir = True
            elif opcion == 4:
                salir = True
            else:
                print("Opción no válida")
                pausar_programa(3)
from src.interfaz.consola import *
from src.interfaz.interface_strings import *
from src.menus.menu_jefe import *
from src.utils.utils import *


def main_menu():
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
                mostrar_menu_empleados()
                pausar_programa(3)
            else:
                print("Opción no válida")
                pausar_programa(3)
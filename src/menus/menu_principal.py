from src.interfaz.consola import *
from src.interfaz.mensajes_menu import *
from src.utils.utils import pedir_numero


def main_menu():
    salir = False

    while not salir:
        mostrar_menu_principal(LOGO)
        opcion = pedir_numero(STRING_GLOBAL_OPCION)
        if opcion == 3:
            print(STRING_EXIT)
            salir = True
        else:
            if opcion == 1:
                nombre = input(STRING_ASK_NAME)
                mostrar_menu_master(nombre)
                input()
            elif opcion == 2:
                mostrar_menu_empleados()
                input()
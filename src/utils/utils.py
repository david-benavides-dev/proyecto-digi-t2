import os
import time

from src.interfaz.interface_strings import *


def limpiar_consola() -> None:
    '''
    Limpia la terminal.
    '''
    if os.name == "nt":
        os.system("cls")  # Comando para limpiar la consola en Windows
    else:
        os.system("clear")  # Comando para limpiar la consola en Unix/Linux


def pedir_numero(msj: str) -> int:
    '''
    
    '''
    numero_validado = False
    while not numero_validado:
        num = input(msj)
        if validar_numero(num):
            numero_validado = True
            return int(num)
        else:
            print("*ERROR* No has introducido un número.")
    pass


def validar_numero(num: str) -> bool:
    '''
    
    '''
    try:
        int(num)
    except ValueError:
        return False
    
    return True


def pausar_programa(tiempo: int = 5, pausa: bool = False) -> None:
    '''
    Pausa el programa

    Args:
        tiempo (int): El tiempo a pausar el programa (por defecto 5).
        pausa (bool): Si deseas pausar el programa hasta que el usuario presione una tecla (por defecto False).
    
    Returns:
        None   
    '''
    if pausa:
        input(STRING_PAUSA)
    if tiempo > 0:
        time.sleep(tiempo)

    return None



def colorear_texto(msj: str, color: str) -> str:
    '''
    Función para cambiar el color a una cadena de caracteres dependiendo de un diccionario clave:valor.

    Args:
        msj (str): El mensaje a colorear.
    '''
    colores = {
        "rojo": "\033[31m",
        "azul": "\033[34m",
        "fin": "\033[0m"
        }

    codigo_color = colores.get(color, colores['fin'])
    return codigo_color + str(msj) + colores['fin']
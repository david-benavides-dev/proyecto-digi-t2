import os
import time

from interfaz.interface_strings import *


def limpiar_consola() -> None:
    """
    Limpia la consola dependiendo del sistema operativo.
    """
    if os.name == "nt":
        os.system("cls")  # Comando para limpiar la consola en Windows
    else:
        os.system("clear")  # Comando para limpiar la consola en Unix/Linux


def pedir_numero(msj: str) -> int:
    """
    Pide al usuario un número válido.
    
    Parámetros:
        msj (str): El mensaje para solicitar el número.
    
    Retorna:
        int: El número ingresado por el usuario.
    """
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
    """
    Valida si una cadena representa un número entero válido.
    
    Parámetros:
        num (str): La cadena a validar.
    
    Retorna:
        bool: True si la cadena es un número válido, False en caso contrario.
    """
    try:
        int(num)
    except ValueError:
        return False
    
    return True


def pausar_programa(tiempo: int = 5, pausa: bool = False) -> None:
    """
    Pausa el programa por un tiempo determinado o hasta que el usuario presione una tecla.

    Parámetros:
        tiempo (int): El tiempo a pausar el programa en segundos (por defecto 5).
        pausa (bool): Si es True, pausa hasta que el usuario presione una tecla (por defecto False).
    
    Retorna:
        None
    """
    if pausa:
        input(STRING_PAUSA)
    if tiempo > 0:
        time.sleep(tiempo)

    return None



def colorear_texto(msj: str, color: str) -> str:
    """
    Colorea un mensaje con el color indicado.

    Parámetros:
        msj (str): El mensaje a colorear.
        color (str): El color para el texto (e.g., 'rojo', 'azul').
    
    Retorna:
        str: El mensaje con el color aplicado.
    """
    colores = {
        "rojo": "\033[31m",
        "azul": "\033[34m",
        "fin": "\033[0m"
        }

    codigo_color = colores.get(color, colores['fin'])
    return codigo_color + str(msj) + colores['fin']
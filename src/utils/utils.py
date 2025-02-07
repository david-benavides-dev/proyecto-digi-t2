import os
import time


def limpiar_consola() -> None:
    '''
    Limpia la terminal.
    '''
    if os.name == "nt":
        os.system("cls")  # Comando para limpiar la consola en Windows
    else:
        os.system("clear")  # Comando para limpiar la consola en Unix/Linux


def pedir_numero() -> int:
    '''
    
    '''
    numero_validado = False
    while not numero_validado:
        num = input("Introduce un número >> ")
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
        input("Pulse una tecla para continuar...")
    if tiempo > 0:
        time.sleep(tiempo)

    return None



def colorear_texto(texto: any, color: str) -> str:
    '''
    Función para cambiar el color a un texto dependiendo de un diccionario clave:valor.

    Args:
        texto (any)
    '''
    colores = {
        "rojo": "\033[31m",
        "azul": "\033[34m",
        "fin": "\033[0m"
        }

    codigo_color = colores.get(color, colores['fin'])
    return codigo_color + str(texto) + colores['fin']
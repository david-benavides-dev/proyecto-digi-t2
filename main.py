from src.interfaz.interface_strings import *
from src.menus.menu_principal import *
from src.sistema.gestion_json import *
from src.sistema.jefes import crear_grupo_tareas, agregar_empleado, gestionar_tareas
from src.utils.utils import *
from src.interfaz import *


def main():
    #main_menu()
    agregar_empleado()
    crear_grupo_tareas()
    gestionar_tareas()
if __name__ == "__main__":
    main()
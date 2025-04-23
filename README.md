<p align="center"><img alt="jobQuest" src="./assets/readme-header.png"/></p>

**JobQuest!** es una herramienta intuitiva diseñada para ayudar a las empresas en la gestión de tareas y objetivos de sus empleados. Utiliza un sistema de puntuación y recompensas basado en el rendimiento, con el objetivo de incentivar la productividad individual de los trabajadores.

La idea surge inspirada en los videojuegos de rol, donde los jugadores deben completar misiones para subir de nivel y obtener recompensas como recursos o equipamiento. **JobQuest!** busca aplicar ese mismo concepto al entorno laboral, convirtiendo los objetivos diarios en "misiones principales" y "misiones secundarias".

> 📝 Nota: Algunas de las funcionalidades descritas en este README pueden no llegar a ser implementadas en la versión final del 
> software debido a limitaciones de tiempo o conocimientos del alumno.

<p align="center">
    <a href="https://david-benavides-dev.github.io/proyecto-digi-t2/docs/">Documentación</a>
    ·
    <a href="https://github.com/david-benavides-dev/proyecto-digi-t2/wiki">Wiki</a>
  </p>

## Tabla de Contenidos

[Motivación](#motivación)

[¿Por qué JobQuest?](#por-qué-jobquest)

[Como Funciona JobQuest](#como-funciona-jobquest)

[Primeros Pasos](#primeros-pasos)

[Ejemplo de uso](#ejemplo-de-uso)

[Tecnologías y Posibles Ampliaciones](#posiblers-ampliaciones)

[Licencia](#licencia)

[Contribuir](#contribuir)

[Referencias](#referencias)

## Motivación
La gestión de tareas en entornos laborales suele resultar poco motivadora. Muchas veces, los empleados no tienen una forma clara de medir su progreso o de recibir reconocimiento por sus logros. JobQuest! nace con el objetivo de cambiar esto, aplicando mecánicas de gamificación inspiradas en los videojuegos de rol para aumentar la implicación y productividad de los empleados.

Este enfoque gamificado tiene como fin transformar las tareas cotidianas en misiones que los empleados deben completar para ganar puntos y obtener recompensas. Al hacerlo, JobQuest! busca fomentar una cultura de rendimiento, autonomía y compromiso.

## ¿Por qué JobQuest?
**JobQuest!** no es solo una herramienta de gestión de tareas, es una plataforma que convierte las responsabilidades laborales en retos. Utilizando un sistema de puntos y recompensas, el empleado tiene incentivos por alcanzar sus metas. Este enfoque va más allá de las herramientas tradicionales de productividad, ya que integra una experiencia gamificada que hace que los trabajadores se sientan más motivados y satisfechos con su rendimiento, aumentando su productividad.

Algunas de las ventajas de JobQuest! incluyen:
- ✅ **Seguimiento de tareas**: Los empleados pueden marcar las tareas que completan en tiempo real.
- ✅ **Claridad de metas**: Cada tarea está claramente definida y categorizada como misión principal o secundaria.
- ✅ **Aumento de la motivación**: Los empleados son incentivados a completar tareas con la promesa de recompensas.
- ✅ **Sistema de puntos**: Los empleados ganan puntos por completar tareas, los cuales pueden canjear por recompensas.
- ✅ **Evaluación**: El jefe puede revisar el progreso de las tareas y validar la puntuación de los empleados.

## Cómo funciona JobQuest

En JobQuest!, los empleados gestionan sus tareas a través de una interfaz simple (actualmente en consola). El proceso básico funciona de la siguiente manera:

Estas tareas estarán creadas y gestionadas por un `master` o empresa, que determinará los objetivos que quiere que el determinado usuario realice.

Una vez completadas, podrán marcarlas, lo que generará un archivo JSON para posterior validación de los mismos por parte del jefe.

Posteriormente, el jefe revisará el progreso y asignará puntos en función del cumplimiento de los objetivos. 

Estos puntos (de ahora en adelante `XP`) podrán utilizarse como 'moneda' interna para obtener beneficios dentro de la empresa.

**Estos son los pasos lógicos que realiza la aplicación:**

1. Un empleado existente en la empresa se conecta en la aplicación.

2. A través de un menú, tendrá opción a descargar tareas dependiendo de la fecha (un archivo JSON), comprobando una lista de tareas a realizar.

3. El usuario podrá comprobar mediante una interfaz (en consola) los objetivos diarios a cumplir, junto a objetivos opcionales (si se han declarado).

4. Una vez finalice, podrá enviar el resultado de su trabajo, generando un archivo JSON que podrá leer el jefe desde su aplicación.
    - Esa información del trabajador incluye: Nombre y `XP` total.

5. Cuando se suba el archivo (por ahora en formato JSON local), el jefe, mediante su aplicación, determinará si esos objetivos se han cumplido. De ser así, podrá modificar la `XP` del empleado dependiendo de los objetivos realizados correctamente.
    - Se actualizará la ficha JSON del trabajador con la `XP` actualizada.

6. El empleado podrá canjear su `XP` por recompensas tales como: día libre, cena, viaje de fin de semana... mediante una opción de su aplicación.

## Primeros Pasos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

### Prerequisitos
Asegurate de tener lo siguiente instalado en tu sistema:
- **Python 3.8** o superior.
- **git** (para clonar el repositorio)
- **Visual Studio Code (VSC)** u otro editor de código.
- **Extensión de Python para Visual Studio Code**: En Visual Studio Code, instala la extensión de Python para habilitar la ejecución de código y el autocompletado. Puedes buscarla en la sección de extensiones de VSC.

### Clonar el repositorio
1. Clona el repositorio:
   ```bash
   git clone https://github.com/david-benavides-dev/proyecto-digi-t2.git
   ```

2. Navega a la carpeta del proyecto:
   ```bash
   cd proyecto-digi-t2
   ```

### Ejecutar el Proyecto
1. Abre Visual Studio Code (VSC) en la carpeta del proyecto.
2. Asegúrate de tener configurado correctamente el PYTHONPATH para que Python pueda resolver correctamente los módulos internos del proyecto.
   Usando los siguientes comandos en la terminal dentro de VSC (CTRL+ALT+ñ):
   Para usuarios de Windows (PowerShell):
   ```bash
   $env:PYTHONPATH="DIRECTORIO_REPO\proyecto-digi-t2\src"
   python main.py
   ```
    Para usuarios de Linux / macOs:
   ```bash
   export PYTHONPATH="/ruta/a/tu/repositorio/proyecto-digi-t2/src"
   python main.py
   ```
> Reemplaza la ruta con la ubicación real donde tienes clonado el repositorio.

## Ejemplo de Uso
- Menú principal
    ```python
    
          _       _      ___                  _   _
         (_) ___ | |__  / _ \ _   _  ___  ___| |_| |
         | |/ _ \| '_ \| | | | | | |/ _ \/ __| __| |
         | | (_) | |_) | |_| | |_| |  __/\__ \ |_|_|
       ,/  |\___/|_.__/ \__\_\__,_|\___||___/\__/(_)
       |__/
    
         ╔═══════════════════════════════════════╗
         ║  1. Login para jefes                  ║
         ║  2. Login para empleados              ║
         ║  3. Salir                             ║
         ╚═══════════════════════════════════════╝
    
    Por favor, seleccione una opción >>
    ```
    Dependiendo de la opción que seleccionemos, nos mostrará un login u otro.
- Menú de jefe/master
    ```python
    
        ╔═══════════════════════════════════════╗
        ║              Hola David               ║
        ╠═══════════════════════════════════════╣
        ║  1. Crear un grupo de tareas          ║
        ║  2. Gestionar tareas de un empleado   ║
        ║  3. Agregar nuevo empleado            ║
        ║  4. Salir                             ║
        ╚═══════════════════════════════════════╝
    
    Por favor, seleccione una opción >>
    ```
    Si seleccionamos la opción 1, pedirá un ID de usuario, en este caso no existen empleados, así que crearemos uno:
    ```python
    
        ╔═══════════════════════════════════════╗
        ║              Hola David               ║
        ╠═══════════════════════════════════════╣
        ║  1. Crear un grupo de tareas          ║
        ║  2. Gestionar tareas de un empleado   ║
        ║  3. Agregar nuevo empleado            ║
        ║  4. Salir                             ║
        ╚═══════════════════════════════════════╝
    
    Por favor, seleccione una opción >> 3
    Perfecto! Empecemos a construir... (introduzca x en cualquier momento para salir)
    Introduce el ID del nuevo empleado: 1
    Introduce el nombre del empleado: Prueba
    Empleado Prueba agregado correctamente.
    ```
    Se creará un archivo JSON en la ruta data/empleados/ID_DEL_EMPLEADO que contendrá los datos del usuario: ID, nombre y experiencia actual del mismo
    Un ejemplo del archivo JSON de empleado creado en el caso anterior:
    ```json
    {
        "worker_id": "1",
        "nombre": "Prueba",
        "xp": 0
    }
    ```
    Ahora podemos crear tareas para dicho empleado utilizando su ID. Esta opción nos pedirá el ID del empleado, el ID del grupo de tareas, la cantidad de tareas que queremos añadir tanto principales como opcionales, así como el nombre de las mismas y la experiencia
    que recibirá el empleado al completarlas. Esta opción también generará un archivo JSON:
  ```python
    ╔═══════════════════════════════════════╗
    ║              Hola David               ║
    ╠═══════════════════════════════════════╣
    ║  1. Crear un grupo de tareas          ║
    ║  2. Gestionar tareas de un empleado   ║
    ║  3. Agregar nuevo empleado            ║
    ║  4. Salir                             ║
    ╚═══════════════════════════════════════╝
  
    Por favor, seleccione una opción >> 1
    Perfecto! Empecemos a construir... (introduzca x en cualquier momento para salir)
    Introduce el ID del empleado: 1
    Introduce un ID para el grupo de misiones: 1
    ¿Cuántas misiones principales desea agregar?: 1
    ¿Cuántas misiones secundarias desea agregar?: 1
    Descripción de la misión principal 1: Trabajar
    XP para la tarea principal 1: 10
    Descripción de la misión secundaria 1: Tarea Opcional Prueba
    XP para la misión secundaria 1: 10
    Grupo de misiones creado correctamente.
  ```
  El archivo JSON generado se guardará en la carpeta con ID del usuario y el nombre será el de grupo de tareas. Este JSON almacenará el nombre de las tareas, el grupo de pertenecer a principal/secundaria, la experiencia que proprciona al usuario y un tag si la tarea se ha     marcado como completada o no por el empleado (que el jefe debe verificar posteriormente)
  Un ejemplo del archivo JSON de las tareas creado en el caso anterior:
  ```json
  {
    "principales": {
        "TID1": {
            "descripcion": "Trabajar",
            "xp": 10,
            "completado": false
        }
    },
    "secundarias": {
        "TID2": {
            "descripcion": "Tarea Opcional Prueba",
            "xp": 10,
            "completado": false
        }
    }
  }
  ```
  También tenemos la opción de gestionar las tareas de un empleado mediante el ID del mismo. De esta forma, validamos una tarea, añadimos XP al usuario y borramos la misma si así lo deseamos:
  ```python
  Introduce el ID del empleado: 1
  MISIONES DE Prueba - ID 1
  -*****************************-
   1
  Introduce la ID del grupo de misiones: 1
  Misiones principales:
  TID1: Trabajar - [X] - 10XP
  Misiones secundarias:
  TID2: Tarea Opcional Prueba - [X] - 10XP
  Introduce la ID de la misión a validar: 1
  Prueba ha conseguido 10 puntos de experiencia. Actualmente tiene 10.
  ¿Desea borrar la misión completada? (S/N): S
  ```
- Menú empleado
  ```python
  Introduce tu ID de empleado: 1

     ╔═══════════════════════════════════════╗
     ║          Hola Prueba - XP: 10         ║
     ╠═══════════════════════════════════════╣
     ║  1. Comprobar tareas                  ║
     ║  2. Marcar tareas                     ║
     ║  3. Visitar la tienda de puntos       ║
     ║  4. Salir                             ║
     ╚═══════════════════════════════════════╝

    Selecciona una opción:
  ```
  Podemos comprobar tareas disponibles, verificar tareas completadas o intercambiar XP por beneficios a cargo de la empresa (NOT YET IMPLEMENTED)
  ```python
     ╔═══════════════════════════════════════╗
     ║          Hola Prueba - XP: 10         ║
     ╠═══════════════════════════════════════╣
     ║  1. Comprobar tareas                  ║
     ║  2. Marcar tareas                     ║
     ║  3. Visitar la tienda de puntos       ║
     ║  4. Salir                             ║
     ╚═══════════════════════════════════════╝

    Selecciona una opción: 1
    Grupo de misiones: 1
    Misiones principales:
    Misiones secundarias:
      TID2: Tarea Opcional Prueba - [X] - 10XP
    Presione una tecla para continuar...
  ```
  Si queremos marcar misiones como completadas, basta con introducir el grupo de misiones que queremos dar como terminadas y el programa se encargará de editar el archivo JSON transformando el boolean a true:
  ```python
     ╔═══════════════════════════════════════╗
     ║          Hola Prueba - XP: 10         ║
     ╠═══════════════════════════════════════╣
     ║  1. Comprobar tareas                  ║
     ║  2. Marcar tareas                     ║
     ║  3. Visitar la tienda de puntos       ║
     ║  4. Salir                             ║
     ╚═══════════════════════════════════════╝

    Selecciona una opción: 2
    Grupos de misiones disponibles:
      1
    Introduce el ID del grupo de misiones que deseas completar: 1
    Has marcado como completado todas las misiones del grupo 1.
  ```
  Dependiendo de la experiencia, podemos cambiar los puntos por recompensas, generando un archivo con una ID automática y haciendo un insert a un sistema interno de la empresa con un ID único (NOT YET IMPLEMENTED)
  ```python
     ╔═══════════════════════════════════════╗
     ║          Hola Prueba - XP: 10         ║
     ╠═══════════════════════════════════════╣
     ║  1. Comprobar tareas                  ║
     ║  2. Marcar tareas                     ║
     ║  3. Visitar la tienda de puntos       ║
     ║  4. Salir                             ║
     ╚═══════════════════════════════════════╝

    Selecciona una opción: 3
    Recompensas disponibles:
      Día libre: 100 XP
      Cena: 200 XP
      Viaje: 500 XP
    ¿Qué deseas canjear? (o escribe 'salir' para volver):
  ```

## Tecnologías y Posibles Ampliaciones
### Tecnologías Utilizadas
- Python: Lenguaje principal para el desarrollo de la aplicación.
- JSON: Para almacenar las tareas y la puntuación de los empleados.

### Posibles Ampliaciones
- **Tkinter**: Biblioteca para la interfaz gráfica de usuario (GUI), para ofrecer una experiencia interactiva más interactiva y visual.

- **Almacenamiento en la nube**: Plataforma en la nube para guardar los archivos, como `Google Drive`, con el fin de hacer la aplicación más accesible y permitir la sincronización de datos en tiempo real.

## Contribuir
¡Las contribuciones a JobQuest! son bienvenidas! Ya sea para mejorar el código, enriquecer la documentación o sugerir nuevas características, tu feedback es valorado. Tienes más información en el archivo [CONTRIBUTING](https://github.com/david-benavides-dev/proyecto-digi-t2/blob/main/CONTRIBUTING.md) para guiarte sobre cómo empezar y hacer que tu contribución cuente.

## Licencia
JobQuest! se publica bajo la licencia MIT. Eres libre de usar, modificar y distribuir el código, tanto para fines comerciales como no comerciales. Para más información, puedes consultar el archivo LICENSE incluido en el repositorio.

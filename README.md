<p align="center"><img alt="jobQuest" src="./assets/readme-header.png"/></p>

**JobQuest!** es una herramienta intuitiva diseñada para ayudar a las empresas en la gestión de tareas y objetivos de sus empleados. Utiliza un sistema de puntuación y recompensas basado en el rendimiento, con el objetivo de incentivar la productividad individual de los trabajadores.

La idea surge inspirada en los videojuegos de rol, donde los jugadores deben completar misiones para subir de nivel y obtener recompensas como recursos o equipamiento. **JobQuest!** busca aplicar ese mismo concepto al entorno laboral, convirtiendo los objetivos diarios en "misiones principales" y "misiones secundarias".

> 📝 Nota: Algunas de las funcionalidades descritas en este README pueden no llegar a ser implementadas en la versión final del 
> software debido a limitaciones de tiempo o conocimientos del alumno.

## Tabla de Contenidos

[Motivación](#motivacion)

[¿Por qué JobQuest?](#porque-jobquest)

[Como Funciona JobQuest](#como-funciona-jobquest)

[Primeros Pasos](#primeros-pasos)

[Posibles Ampliaciones](#posiblers-ampliaciones)

[Licencia](#licencia)

[Contribuir](#contribuir)

[Referencias](#referencias)


## Tecnologías utilizadas

- **Python**: Lenguaje principal para el desarrollo de la aplicación.

- **JSON**: Formato de archivo utilizado para almacenar las tareas y puntuaciones.

> 💡 Características que podrían ser implementadas en versiones posteriores:

- **Tkinter**: Biblioteca para la interfaz gráfica de usuario (GUI), para ofrecer una experiencia interactiva más rica.

- **Cloud Storage**: Plataforma en la nube para guardar los archivos, como `Google Drive`, con el fin de hacer la aplicación más accesible y permitir la sincronización de datos en tiempo real.

## Características principales

- ✅ **Seguimiento de tareas**: Los empleados pueden marcar las tareas que completan en tiempo real.
- ✅ **Sistema de puntos**: Los empleados ganan puntos por completar tareas, los cuales pueden canjear por recompensas.
- ✅ **Evaluación**: El jefe puede revisar el progreso de las tareas y validar la puntuación de los empleados.

## Cómo funciona

Los empleados podrán gestionar tareas a través de una interfaz (en este caso, se utilizará una simple consola en la versión inicial).

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

# Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu máquina:

1. **Python 3.x**
2. **Visual Studio Code**
    
Si tienes Python, descárgalo desde python.org.

3. **Visual Studio Code**: Si aún no lo tienes, puedes descargar Visual Studio Code desde su web oficial.

4. **Extensión de Python para Visual Studio Code**: En Visual Studio Code, instala la extensión de Python para habilitar la ejecución de código y el autocompletado. Puedes buscarla en la sección de extensiones de VSC.

# Pasos para ejecutar el proyecto

1. Clonar el repositorio https://github.com/david-benavides-dev/proyecto-digi-t2.git desde la interfaz de VSC o mediante comandos.
2. Navega a la carpeta del proyecto.
3. Ejecutar main.py (run python file, botón de "Play" arriba a la derecha)

# Licencia
JobQuest! se publica bajo la licencia MIT.

Esto significa que eres libre de usar, modificar y distribuir el código, tanto para fines comerciales como no comerciales, siempre que se incluya una copia del aviso de copyright original y la licencia en cualquier copia del software o parte sustancial del mismo.

Para más información, puedes consultar el archivo LICENSE incluido en el repositorio.

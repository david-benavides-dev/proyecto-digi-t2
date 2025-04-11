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
2. Ejecuta el archivo principal main.py.
   Puedes hacerlo directamente desde VSC usando el botón "Run" (el botón de "Play en la parte superior derecha) o usando el siguiente comando en la terminal:
   ```bash
   python main.py
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

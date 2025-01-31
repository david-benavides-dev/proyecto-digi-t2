<p align="center"><img alt="jobQuest" src="./assets/readme-header.png"/></p>

# jobQuest! - Gestión de Objetivos y Tareas para Empresas
**JobQuest!** pretende ser una herramienta intuitiva diseñada para ayudar a las empresas en la gestión de tareas y objetivos de sus empleados. Utiliza un sistema de puntuación y recompensas basado en el rendimiento, con el objetivo de incentivar la productividad individual de los trabajadores.

La idea surge inspirada en los videojuegos de rol, donde los jugadores deben completar misiones para subir de nivel y obtener recompensas como recursos o equipamiento. **JobQuest!** busca aplicar ese mismo concepto al entorno laboral, convirtiendo los objetivos diarios en "misiones principales" y "misiones secundarias".

> 📝 Nota: Algunas de las funcionalidades descritas en este README pueden no llegar a ser implementadas en la versión final del 
> software debido a limitaciones de tiempo o conocimientos del alumno.

## Tecnologías utilizadas

- **Python**: Lenguaje principal para el desarrollo de la aplicación.

- **Tkinter**: Biblioteca para la interfaz gráfica de usuario (GUI).

- **JSON**: Formato de archivo utilizado para almacenar las tareas y puntuaciones.

- **Cloud Storage**: Plataforma en la nube para guardar los archivos (probablemente Google Drive).

## Características principales

- ✅ **Seguimiento de tareas**: Los empleados pueden marcar las tareas que completan en tiempo real.
- ✅ **Sistema de puntos**: Los empleados ganan puntos por completar tareas, los cuales pueden canjear por recompensas.
- ✅ **Interfaz fácil de usar**: Diseñada con Tkinter para una experiencia simple e interactiva.
- ✅ **Subida automática a la nube**: Los archivos JSON se suben a la nube para mantener un registro seguro y accesible.
- ✅ **Evaluación**: El jefe puede revisar el progreso de las tareas y validar la puntuación de los empleados.

## Cómo funciona

Los empleados podrán gestionar tareas a través de una interfaz.

Estas tareas estarán creadas y gestionadas por un `master` o empresa, que determinará los objetivos que quiere que el determinado usuario realice.

Una vez completadas, podrán marcarlas y enviarlas al sistema, donde se registrarán en un archivo JSON que se subirá a la nube. 

Posteriormente, el jefe revisará el progreso y asignará puntos en función del cumplimiento de los objetivos. 

Estos puntos (de ahora en adelante `XP`) podrán utilizarse como 'moneda' interna para obtener beneficios dentro de la empresa.

**Estos son los pasos lógicos que la realiza la aplicación:**

1. Un empleado existente en la empresa se conecta en la aplicación y se valida que es un empleado de la misma.

2. Automáticamente, el programa descargará un JSON basándose en el ID único del usuario con la información del trabajador. Además, podrá comprobar si existe una lista de tareas a realizar.
    - Esa información del trabajador incluye: Nombre, Empresa, Puesto y `XP` total.
    - La lista de tareas estará disponible mediante un ID único que el jefe deberá proporcionar a su empleado indivualmente.

3. El usuario podrá comprobar mediante una interfaz gráfica los objetivos diarios a cumplir, junto a objetivos opcionales (si se han declarado).

4. Una vez finalice, podrá enviar el resultado de su trabajo.

5. Cuando se suba el archivo a la nube, el jefe determinará si esos objetivos se han cumplido. De ser así, modificará la `XP` del empleado dependiendo de los objetivos realizados correctamente.

6. El empleado podrá canquejar su `XP` por recompensas tales como: día libre, cena, viaje de fin de semana...
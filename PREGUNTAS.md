# Preguntas a responder
## Ciclo de vida del dato (5b):

### ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
Los datos se generan cuando un empleado recibe y completa tareas, luego se guardan en archivos JSON. Estos datos se actualizan cuando el jefe revisa las tareas y asigna puntos.
### ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?
La integridad se mantiene mediante la actualización de los archivos JSON solo al completar tareas verificadas. No se pierden datos previos al añadir nuevas tareas.
### Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?
En el futuro, se podría integrar una base de datos ligera como SQLite para mejorar la gestión de datos y consultas.

## Almacenamiento en la nube (5f):

### Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?
Para garantizar la seguridad, se usarían plataformas con encriptación y autenticación de usuarios (por ejemplo, Google Drive o AWS).
### ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?
Inicialmente se usan archivos JSON locales por simplicidad y falta de conocimiento. La nube podría implementarse para mejorar la accesibilidad y sincronización entre empleado/jefe.
### Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?
Probablemente usaría APIs de servicios en la nube (Google Drive, Dropbox) para permitir la sincronización automática de datos.

## Seguridad y regulación (5i):

### ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?
Actualmente no se implementa seguridad avanzada, pero en futuras versiones se podría usar encriptación y autenticación de usuarios.
### ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?
El software debería cumplir con el GDPR, solicitando consentimiento explícito de los usuarios y permitiendo la eliminación de sus datos.
### Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?
Los riesgos incluyen pérdida de datos y acceso no autorizado. A futuro, se se podría implementar cifrado y autenticación de usuarios. Uno de los mayores problemas de la fase temprana de la aplicación es la capacidad del trabajador de manipular los archivos JSON, hacerse pasar por otro empleado, etc...

## Implicación de las THD en negocio y planta (2e):

### ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?
Mejoraría la productividad de los empleados mediante la gamificación de tareas y objetivos.
### ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?
Facilitando el seguimiento del rendimiento de los empleados y optimizando la asignación de tareas.
### Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?
El software puede ser útil en equipos de desarrollo, educación o voluntariado, donde las tareas deben ser gestionadas y recompensadas.

## Mejoras en IT y OT (2f):

### ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?
Aunque no es específico para IT y OT, podría integrarse con plataformas de gestión empresarial para mejorar la eficiencia en la asignación de tareas.
### ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?
La asignación automática de tareas y la sincronización de datos mejoraría la eficiencia operativa.
### Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?
El software podría integrarse con sistemas ERP o de producción para optimizar los procesos en IT y OT.

## Tecnologías Habilitadoras Digitales (2g):

### ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?
Actualmente, se usa Python y JSON. En el futuro, se podrían integrar APIs de almacenamiento en la nube y herramientas de análisis de datos.
### ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?
El uso de APIs y herramientas de análisis de datos mejoraría la accesibilidad y proporcionaría informes detallados sobre el rendimiento.
### Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?
Se podrían integrar tecnologías como Big Data o Machine Learning para mejorar la gestión y automatización de tareas a gran escala.

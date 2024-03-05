# Aplicación de Gestión de Tareas

## Descripción

La Aplicación de Gestión de Tareas es un proyecto que permite a los usuarios crear, organizar y seguir el progreso de sus tareas y proyectos.

## Estructura del Proyecto

El proyecto deberá tener la siguiente estructura de archivos y directorios:

``` markdown
gestion_tareas/
    __init__.py
    tareas/
        __init__.py
        tarea.py
        tarea_personal.py
        tarea_proyecto.py
    proyectos/
        __init__.py
        proyecto.py
    usuarios/
        __init__.py
        usuario.py
    __main__.py
README.md
```
- **tareas/:** Directorio que contiene las clases relacionadas con las tareas.
  - **tarea.py:** Archivo que contiene la definición de la clase base Tarea.
  - **tarea_personal.py:** Archivo que contiene la definición de la clase TareaPersonal.
  - **tarea_proyecto.py:** Archivo que contiene la definición de la clase TareaProyecto.
- **proyectos/:** Directorio que contiene las clases relacionadas con los proyectos.
  - **proyecto.py:** Archivo que contiene la definición de la clase Proyecto.
- **usuarios/:** Directorio que contiene las clases relacionadas con los usuarios.
  - **usuario.py:** Archivo que contiene la definición de la clase Usuario.
- **__main__.py:** Archivo principal que contiene el punto de entrada del programa.

## Ejecución del Proyecto

Para ejecutar la Aplicación de Gestión de Tareas, sigue los siguientes pasos:

- Abre una terminal.
- Navega hasta el directorio raíz del proyecto general.
- Ejecuta el siguiente comando: **python -m gestion_tareas**.

Con esto, podrás disfrutar de la funcionalidad ofrecida por la Aplicación de Gestión de Tareas. ¡Que lo disfrutes!
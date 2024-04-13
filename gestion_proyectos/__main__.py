from .equipos.equipo import Team, User
from .proyectos.proyecto import Project
from .tareas.tarea import Task

def main():
    print("\n\t######################   Módulo de tareas   ####################")
    print("\n####### Creacón de los miembros del equipo: ##########")
    pablo = User("Pablo Pérez Martínez", "paperez@puce.edu.ec")
    juan = User("Juan Gonzalez", "jjgonzalez@puce.edu.ec")
    print(juan, pablo, sep="\n")
    
    print("\n####### Creacón del equipo: ##########")
    equipo_desarrollo = Team("Desarrollo", [juan, pablo])
    print(f"\nSe agrega a {juan.name} y a {pablo.name} al equipo: ", equipo_desarrollo)
    
    print("\n####### Creación e inicio del proyecto: ##########")
    proyecto_movil = Project("Aplicación Móvil")
    proyecto_movil.start_project()
    
    print("\n####### Creación de las tareas: ##########")
    task = Task("Generar Mockups", equipo_desarrollo, proyecto_movil)
    print("\nSe crea la tarea", task)
    task2 = Task("Crear Login", equipo_desarrollo, proyecto_movil)
    print("\nSe crea la tarea", task2)
    
    print("\n####### Inicio de las tareas: ##########")
    task.start_task()
    task2.start_task()
    
    print("\n####### Finalización de las tareas: ##########")
    task.finish_task()
    task2.finish_task()
    
    print("\n####### Finalización del proyecto: ##########")
    proyecto_movil.finish_project()

if __name__ == "__main__":
    main()

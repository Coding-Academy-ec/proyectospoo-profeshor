# Archivo: gestion_tareas/__main__.py
from gestion_tareas.tareas.tarea_personal import TareaPersonal
from gestion_tareas.tareas.tarea_proyecto import TareaProyecto

def main():
    # Crear algunas tareas personales
    tarea_personal1 = TareaPersonal("Comprar víveres", "Ir al supermercado y comprar los víveres para la semana", "2024-03-10", "Alta")
    tarea_personal2 = TareaPersonal("Hacer ejercicio", "Ir al gimnasio y hacer ejercicio durante una hora", "2024-03-08", "Media")

    # Crear algunas tareas de proyecto
    tarea_proyecto1 = TareaProyecto("Diseñar interfaz de usuario", "Diseñar la interfaz de usuario para la nueva aplicación móvil", "2024-03-15", "Equipo de diseño")
    tarea_proyecto2 = TareaProyecto("Implementar backend", "Implementar la lógica del backend utilizando Django", "2024-03-20", "Equipo de desarrollo")

    # Mostrar detalles de las tareas
    print("Tareas personales:")
    print(tarea_personal1)
    print(tarea_personal2)

    print("\nTareas de proyecto:")
    print(tarea_proyecto1)
    print(tarea_proyecto2)

if __name__ == "__main__":
    main()

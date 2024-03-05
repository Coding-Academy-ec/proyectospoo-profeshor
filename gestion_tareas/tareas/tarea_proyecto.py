# Archivo: gestion_tareas/tareas/tarea_proyecto.py
from .tarea import Tarea

class TareaProyecto(Tarea):
    def __init__(self, nombre, descripcion, fecha_limite, asignado_a):
        super().__init__(nombre, descripcion, fecha_limite)
        self.asignado_a = asignado_a

    def __str__(self):
        return f"Tarea de Proyecto: {super().__str__()}, Asignado a: {self.asignado_a}"
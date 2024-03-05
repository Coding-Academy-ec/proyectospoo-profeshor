# Archivo: gestion_tareas/tareas/tarea_personal.py
from .tarea import Tarea

class TareaPersonal(Tarea):
    def __init__(self, nombre, descripcion, fecha_limite, prioridad):
        super().__init__(nombre, descripcion, fecha_limite)
        self.prioridad = prioridad

    def __str__(self):
        return f"Tarea Personal: {super().__str__()}, Prioridad: {self.prioridad}"




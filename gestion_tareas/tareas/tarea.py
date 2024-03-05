# Archivo: gestion_tareas/tareas/tarea.py

class Tarea:
    def __init__(self, titulo, descripcion, fecha_limite):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite

    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nFecha límite: {self.fecha_limite}"

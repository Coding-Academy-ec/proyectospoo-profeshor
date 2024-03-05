# Archivo: gestion_tareas/usuarios/usuario.py
class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Usuario: {self.nombre}, Correo: {self.correo}"

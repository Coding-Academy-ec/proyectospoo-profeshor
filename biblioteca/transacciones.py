# Archivo: biblioteca/transacciones.py

from .usuarios import Usuario
from .libros import Libro

class Transaccion:
    def __init__(self, usuario: Usuario, libro: Libro, fecha_prestamo):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo

    def prestar(self):
        self.libro.status = "Prestado"
        print (f"El libro {self.libro.titulo} ha sido prestado al usuario {self.usuario.nombre}")
        pass

    def devolver(self):
        # Lógica para devolver un libro
        self.libro.status = "Disponible"
        print (f"El libro {self.libro.titulo} ha sido devuelto por el usuario {self.usuario.nombre}")
        pass

    def __str__(self):
        return f"Transacción: Usuario: {self.usuario.nombre}, Libro: {self.libro.titulo}, Fecha de Préstamo: {self.fecha_prestamo}"

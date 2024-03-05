# Archivo: biblioteca/transacciones.py

class Transaccion:
    def __init__(self, usuario, libro, fecha_prestamo):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo

    def prestar(self):
        # Lógica para prestar un libro
        pass

    def devolver(self):
        # Lógica para devolver un libro
        pass

    def __str__(self):
        return f"Transacción: Usuario: {self.usuario.nombre}, Libro: {self.libro.titulo}, Fecha de Préstamo: {self.fecha_prestamo}"

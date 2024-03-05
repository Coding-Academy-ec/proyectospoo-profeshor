# Archivo: biblioteca/libros.py

class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

class LibroPrestado(Libro):
    def __init__(self, isbn, titulo, autor, prestado_a):
        super().__init__(isbn, titulo, autor)
        self.prestado_a = prestado_a

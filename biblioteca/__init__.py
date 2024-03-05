# Archivo: biblioteca/__init__.py

# Importar las clases necesarias desde los submódulos
from .libros import Libro
from .usuarios import Usuario
from .transacciones import Transaccion

# Punto de entrada del programa
def main():
    # Crear algunos libros
    libro1 = Libro("1234567890", "Python Programming", "Guido van Rossum")
    libro2 = Libro("0987654321", "Clean Code", "Robert C. Martin")

    # Crear algunos usuarios
    usuario1 = Usuario("1001", "Alice")
    usuario2 = Usuario("1002", "Bob")

    # Realizar algunas transacciones
    transaccion1 = Transaccion(usuario1, libro1)
    transaccion1.prestar()
    transaccion2 = Transaccion(usuario2, libro2)
    transaccion2.prestar()

    # Mostrar detalles de las transacciones
    print("Transacciones realizadas:")
    for transaccion in [transaccion1, transaccion2]:
        print(transaccion)

if __name__ == "__main__":
    main()


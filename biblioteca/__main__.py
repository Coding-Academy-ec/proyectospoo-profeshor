from biblioteca.libros import Libro
from biblioteca.usuarios import Usuario
from biblioteca.transacciones import Transaccion

def main():
    # Crear algunos libros
    print ("****** Ingreso un libro ******")
    #libro1 = Libro("1234567890", "Python Programming", "Guido van Rossum")
    libro1 = Libro(
        input("Ingresar ISBN del libro: "),
        input("Ingresar título del libro: "),
        input("Ingresar autor del libro: ")
    )

    # Crear algunos usuarios
    print ("****** Ingreso un usuario ******")
    usuario1 = Usuario(
        input("Ingresa código de usuario: "),
        input("Ingresa Nombre del usuario: ")
    )

    # Fecha de préstamo
    fecha_prestamo = "2024-03-10"  # Por ejemplo, fecha actual

    # Realizar algunas transacciones
    transaccion1 = Transaccion(usuario1, libro1, fecha_prestamo)
    transaccion1.prestar()
    print("El libro está prestado")

    # Mostrar detalles de las transacciones
    print("Transacciones realizadas:")
    for transaccion in [transaccion1]:
        print(transaccion)

if __name__ == "__main__":
    main()

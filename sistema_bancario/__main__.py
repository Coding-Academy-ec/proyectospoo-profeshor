# Archivo: sistema_bancario/__main__.py
from sistema_bancario.clientes.cliente import Cliente
from sistema_bancario.empleados.empleado import Empleado
from sistema_bancario.transacciones.transaccion import Transaccion

def main():
    # Crear clientes
    cliente1 = Cliente("Alice", "123 Main St", 1000)
    cliente2 = Cliente("Bob", "456 Elm St", 2000)

    # Crear empleados
    empleado1 = Empleado("Eva", "Gerente", 5000)
    empleado2 = Empleado("Alex", "Cajero", 3000)

    # Realizar transacciones
    transaccion1 = Transaccion(cliente1.nombre, cliente2.nombre, 500)
    transaccion2 = Transaccion(empleado2.nombre, cliente1.nombre, 200)

    # Mostrar detalles de las transacciones
    print("Transacciones realizadas:")
    print(transaccion1)
    print(transaccion2)

if __name__ == "__main__":
    main()

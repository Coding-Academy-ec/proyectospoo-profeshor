# Archivo: sistema_bancario/empleados/empleado.py

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Empleado: {self.nombre}\nCargo: {self.cargo}\nSalario: {self.salario}"

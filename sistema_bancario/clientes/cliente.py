# Archivo: sistema_bancario/clientes/cliente.py

class Cliente:
    def __init__(self, nombre, direccion, saldo):
        self.nombre = nombre
        self.direccion = direccion
        self.saldo = saldo

    def __str__(self):
        return f"Cliente: {self.nombre}\nDirección: {self.direccion}\nSaldo: {self.saldo}"

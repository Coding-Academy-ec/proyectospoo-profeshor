# Archivo: sistema_bancario/transacciones/transaccion.py

class Transaccion:
    def __init__(self, origen, destino, monto):
        self.origen = origen
        self.destino = destino
        self.monto = monto

    def __str__(self):
        return f"Transacción: Origen: {self.origen}, Destino: {self.destino}, Monto: {self.monto}"

"""
Autor: Pablo Pérez Martínez
"""
from datetime import datetime

class Project:
    """
    Clase para manejo de proyectos
    """
    def __init__(self, name:str) -> None:
        self.name = name
        self.date_created = datetime.now()
        self.date_modified = datetime.now()
        self.status = "creado"
        
    def __str__(self) -> str:
        return f"Proyecto {self.name}"
        
    def start_project(self):
        self.status = "Iniciado"
        self.date_modified = datetime.now()
        print(f"El proyecto {self.name} se ha iniciado")
        
    def finish_project(self):
        self.status = "Finalizado"
        self.date_modified = datetime.now()
        print(f"El proyecto {self.name} ha finalizado")
from ..equipos.equipo import Team
from ..proyectos.proyecto import Project

class Task:
    """
    Clase de manejo de tareas
    """
    def __init__(self, name: str, asignee: Team, project: Project) -> None:
        self.name = name
        self.status = "En cola"
        self.asignee = asignee
        self.project = project
        
    def __str__(self) -> str:
        return f'Tarea: {self.name}\nAsignada a: {self.asignee.team_name}\nEstado: {self.status}\nProyecto: {self.project}'
    
    def set_asignee(self, asignee: Team):
        self.asignee = asignee
        print(f'La tarea: {self.name} se ha asignado al equipo {self.asignee.team_name}')
        
    def start_task(self):
        self.status="En curso"
        print(f'La tarea {self.name} tiene un estado: {self.status}')
        
    def finish_task(self):
        self.status="Finalizado"
        print(f'La tarea {self.name} tiene un estado: {self.status}')
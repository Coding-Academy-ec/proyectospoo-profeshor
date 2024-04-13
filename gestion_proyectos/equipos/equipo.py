class User:
    """
    Clase usuario
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Usuario: {self.name}, Correo: {self.email}"

class Team:
    """
    Clase equipo
    """
    def __init__(self, team_name:str, users: list[User]) -> None:
        self.team_name = team_name
        self.users = users
        
    def __str__(self) -> str:
        return f"{self.team_name}"
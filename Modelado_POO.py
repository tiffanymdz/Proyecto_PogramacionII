class Jugador:
    def __init__(self, name, team, position, minutes, goals, assists):
        self.name = name
        self.team = team
        self.position = position
        self.minutes = minutes
        self.goals = goals
        self.assists = assists

class Equipo:
    def __init__(self, name, liga="Premier League"):
        self.name = name
        self.liga = liga
        self.jugadores = []

    def agregar_jugador(self,jugador):
        self.jugadores.append(jugador)

    def total_goles(self):
        total = 0
        for jugador in self.jugadores:
            total += jugador.goals
        return total

    def total_assists(self):
        total = 0
        for jugador in self.jugadores:
            total += jugador.assists
        return total
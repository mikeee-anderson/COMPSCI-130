class CricketTeam:
    def __init__(self, team_name="N/A", players=None, ):
        if players is None:
            players = []
        self.team_name = team_name
        self.players = players
    def add_player(self, player):
        self.players.append(player)
    def remove_player(self, name):
        if name in self.players:
            self.players.remove(name)
    def __str__(self):
        sorted_players = sorted(self.players)
        return f"{self.team_name}:{', '.join(sorted_players)}"

team1 = CricketTeam("NZ")
team1.add_player("Michael")
team1.add_player("Bob")
print(team1)
print(team1.players)
team1.remove_player("Bob")
print(team1)
team1.remove_player("David")
print(team1)



class CricketTeam:
    def __init__(self, team_name="N/A", players=None, ):
        if players is None:
            players = []

        self.team_name = team_name
        self.players = players
    def add_player(self, player):
        self.players.append(player)

team1 = CricketTeam()
team2 = CricketTeam("NZ")
team1.add_player("Bob")
team2.add_player("Michael")
print(team1.team_name, team1.players)
print(team2.team_name, team2.players)
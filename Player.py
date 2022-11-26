import uuid

from Scoreboard import Scoreboard


class Player:
    def __init__(self, name, actions_per_turn):
        self.id = str(uuid.uuid4())
        self.name = name
        self.scoreboard = Scoreboard()
        self.is_current_turn = False
        self.actions_per_turn = actions_per_turn

    # def add_players(self):
    #     print("Player 1 name: ")
    #     self.player_one = Player(input())
    #     print("Player 2 name: ")
    #     self.player_two = Player(input())

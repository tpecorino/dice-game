import random

from GamePiece import Die
from Player import Player
from RollChecker import RollChecker


class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.current_player = None
        self.game_piece = Die(6)
        self.game_ended = False
        self.roll_checker = RollChecker()

    def setup(self):
        print("Player 1 name: ")
        self.player_one = Player(input())
        print("Player 2 name: ")
        self.player_two = Player(input())

        first_player = random.choice(self.get_players())
        first_player.is_current_turn = True
        self.current_player = first_player
        return

    def get_players(self):
        return self.player_one, self.player_two

    def change_turn(self):
        if self.player_one.is_current_turn:
            self.player_one.is_current_turn = False
            self.player_two.is_current_turn = True
            self.current_player = self.player_two
        else:
            self.player_one.is_current_turn = True
            self.player_two.is_current_turn = False
            self.current_player = self.player_one

    def player_roll(self):
        die_roll_count = 5
        dice_roll = []
        for i in range(die_roll_count):
            roll = self.game_piece.roll()
            dice_roll.append(roll)

        self.roll_checker.check(dice_roll, self.current_player.scoreboard)
        self.change_turn()
        return


if __name__ == "__main__":
    game = Game()
    game.setup()
    game.player_roll()
    print(game)

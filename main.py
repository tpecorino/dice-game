import random

from GamePiece import Die
from Player import Player
from RollChecker import RollChecker
from Scoreboard import Scoreboard
from dialog import choice_dialog


class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.current_player = None
        self.end_turn = False
        self.game_piece = Die(6)
        self.game_in_progress = False
        self.roll_checker = RollChecker()
        self.temp_scoreboard = Scoreboard()

    def setup(self):
        print("Player 1 name: ")
        self.player_one = Player(input(), 3)
        print("Player 2 name: ")
        self.player_two = Player(input(), 3)

    def start_game(self):
        first_player = random.choice(self.get_players())
        first_player.is_current_turn = True
        self.current_player = first_player
        self.game_in_progress = True

    def get_players(self):
        return self.player_one, self.player_two

    def change_turn(self):
        if self.player_one.is_current_turn:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one
        self.end_turn = False

    def player_roll(self):
        die_roll_count = 5
        dice_roll = []

        if self.current_player.actions_per_turn and not self.end_turn:
            for i in range(die_roll_count):
                roll = self.game_piece.roll()
                dice_roll.append(roll)

            print(dice_roll)

            self.roll_checker.check(dice_roll, self.temp_scoreboard)
            self.current_player.actions_per_turn -= 1
            temp_roll_board = self.temp_scoreboard.__dict__
            for idx, result in enumerate(iter(temp_roll_board)):
                print(f'{idx + 1}. {result}: {temp_roll_board[result]}')

            if self.current_player.actions_per_turn:
                print("Roll again?\n 1: Yes \n 2: No")
                response = input()
                if response == '1':
                    self.player_roll()
                elif response == '2':
                    self.end_turn = True
                    return self.temp_scoreboard.__dict__
                elif response == 'end':
                    self.game_in_progress = False
        else:
            self.change_turn()
        return self.temp_scoreboard.__dict__

    def select_score(self, roll_board):
        result = choice_dialog(roll_board)
        self.current_player.scoreboard.__setitem__(result, roll_board[result])
        self.change_turn()
        pass


if __name__ == "__main__":
    game = Game()
    game.setup()
    game.start_game()

    while game.game_in_progress is True:
        final_roll_board = game.player_roll()
        game.select_score(final_roll_board)
    print("End Turn")

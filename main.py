from GameBoard import Scoreboard, Combo
from GamePiece import Die
from RollChecker import RollChecker

if __name__ == "__main__":
    die = Die(6)
    die_roll_count = 5
    dice_roll = []

    for i in range(die_roll_count):
        roll = die.roll()
        dice_roll.append(die.roll())

    roll_checker = RollChecker()
    # outcome = roll_checker.check(dice_roll)

    print(dice_roll)
    # print(outcome)

    player_1_scoreboard = Scoreboard(1)
    player_2_scoreboard = Scoreboard(2)

    outcome = roll_checker.check(dice_roll, player_1_scoreboard)

    sb = iter(player_1_scoreboard)

    print(sb)

    print(next(sb))

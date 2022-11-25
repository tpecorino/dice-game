import unittest
from RollChecker import RollChecker
from Scoreboard import Scoreboard


class TestRollChecker(unittest.TestCase):
    def test_dice_match_combo(self):
        """
        Test that it can identify single dice combos
        """
        scoreboard = Scoreboard()
        roll = [5, 5, 3, 5, 6]
        roll_checker = RollChecker()
        roll_checker.check(roll, scoreboard)
        self.assertEqual(scoreboard.five_combo_score, 15)
        self.assertEqual(scoreboard.six_combo_score, 6)
        self.assertEqual(scoreboard.two_combo_score, 0)

    def test_three_of_a_kind(self):
        """
        Test that it can identify a three of a kind
        """
        scoreboard = Scoreboard()
        roll = [5, 5, 3, 5, 6]
        roll_checker = RollChecker()
        result = roll_checker.check(roll, scoreboard)
        self.assertTrue(result["three_of_kind"])

    def test_four_of_a_kind(self):
        """
        Test that it can identify a four of a kind which also will have a three of a kind
        """
        scoreboard = Scoreboard()
        roll = [5, 5, 3, 5, 5]
        roll_checker = RollChecker()
        result = roll_checker.check(roll, scoreboard)
        self.assertTrue(result["three_of_kind"])
        self.assertTrue(result["four_of_kind"])

    def test_small_straight(self):
        """
        Test that it can identify a small straight
        """
        scoreboard = Scoreboard()
        roll = [2, 5, 3, 4, 5]
        roll_checker = RollChecker()
        result = roll_checker.check(roll, scoreboard)
        self.assertTrue(result["small_straight"])

    def test_large_straight(self):
        """
        Test that it can identify a large straight which also will have a small straight
        """
        scoreboard = Scoreboard()
        roll = [2, 6, 3, 4, 5]
        roll_checker = RollChecker()
        result = roll_checker.check(roll, scoreboard)
        self.assertTrue(result["small_straight"])
        self.assertTrue(result["large_straight"])

    def test_five_of_a_kind(self):
        """
        Test that it can identify a five of a kind which also will have a three and four of a kind
        """
        scoreboard = Scoreboard()
        roll = [5, 5, 5, 5, 5]
        roll_checker = RollChecker()
        result = roll_checker.check(roll, scoreboard)
        self.assertTrue(result["three_of_kind"])
        self.assertTrue(result["four_of_kind"])
        self.assertTrue(result["five_of_kind"])


if __name__ == '__main__':
    unittest.main()

import unittest
from RollChecker import RollChecker


class TestRollChecker(unittest.TestCase):
    def test_dice_match_combo(self):
        """
        Test that it can identify single dice combos
        """
        roll = [5, 5, 3, 5, 6]
        roll_checker = RollChecker()
        result = roll_checker.check(roll)
        self.assertEqual(result["five_combo_score"], 15)
        self.assertEqual(result["six_combo_score"], 6)
        self.assertEqual(result["two_combo_score"], 0)

    def test_three_of_a_kind(self):
        """
        Test that it can identify a three of a kind
        """
        roll = [5, 5, 3, 5, 6]
        roll_checker = RollChecker()
        result = roll_checker.check(roll)
        self.assertTrue(result["three_of_kind"])

    def test_four_of_a_kind(self):
        """
        Test that it can identify a four of a kind which also will have a three of a kind
        """
        roll = [5, 5, 3, 5, 5]
        roll_checker = RollChecker()
        result = roll_checker.check(roll)
        self.assertTrue(result["three_of_kind"])
        self.assertTrue(result["four_of_kind"])

    def test_small_straight(self):
        """
        Test that it can identify a small straight
        """
        roll = [2, 5, 3, 4, 5]
        roll_checker = RollChecker()
        result = roll_checker.check(roll)
        self.assertTrue(result["small_straight"])

    def test_large_straight(self):
        """
        Test that it can identify a large straight which also will have a small straight
        """
        roll = [2, 6, 3, 4, 5]
        roll_checker = RollChecker()
        result = roll_checker.check(roll)
        self.assertTrue(result["small_straight"])
        self.assertTrue(result["large_straight"])

    def test_five_of_a_kind(self):
        """
        Test that it can identify a five of a kind which also will have a three and four of a kind
        """
        roll = [5, 5, 5, 5, 5]
        roll_checker = RollChecker()
        result = roll_checker.check(roll)
        self.assertTrue(result["three_of_kind"])
        self.assertTrue(result["four_of_kind"])
        self.assertTrue(result["five_of_kind"])


if __name__ == '__main__':
    unittest.main()

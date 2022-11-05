class Scoreboard:
    def __init__(self, player_id):
        self.player_id = player_id
        self.one_combo = Combo("Ones", "Sum of the dice", 0, True)
        self.two_combo = Combo("Twos", "Sum of the dice", 0, True)
        self.three_combo = Combo("Threes", "Sum of the dice", 0, True)
        self.four_combo = Combo("Fours", "Sum of the dice", 0, True)
        self.five_combo = Combo("Fives", "Sum of the dice", 0, True)
        self.six_combo = Combo("Sixes", "Sum of the dice", 0, True)
        self.bonus = Combo("Bonus", "Sum of the dice", 0, True)
        self.three_of_kind = Combo("Three of a kind", "Sum of the dice", 0, True)
        self.four_of_kind = Combo("Four of a kind", "Sum of the dice", 0, True)
        self.full_house = Combo("Full house", "25 points", 0, True)
        self.small_straight = Combo("Small straight", "30 points", 0, True)
        self.large_straight = Combo("Large straight", "40 points", 0, True)
        self.five_of_kind = Combo("Five of a kind", "50 points", 0, True)
        self.chance = Combo("Chance", "Sum of the dice", 0, True)

    def __iter__(self):
        return self

    def __next__(self):

        return self

    def get_scoreboard(self):
        return self.__dict__

    def update_scoreboard(self, combo):
        pass


class Combo:
    def __init__(self, label, description, score, is_locked):
        self.label = label
        self.description = description
        self.score = score
        self.is_locked = is_locked

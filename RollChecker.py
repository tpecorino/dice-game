class RollChecker:
    def __init__(self):
        self.roll = []
        self.two_of_kind = False
        self.three_of_kind = False
        self.four_of_kind = False
        self.full_house = False
        self.small_straight = False
        self.large_straight = False
        self.five_of_kind = False

    def check(self, roll, scoreboard):
        self.roll = roll
        scoreboard.one_combo_score = roll.count(1) * 1 if roll.count(1) else 0
        scoreboard.two_combo_score = roll.count(2) * 2 if roll.count(2) else 0
        scoreboard.three_combo_score = roll.count(3) * 3 if roll.count(3) else 0
        scoreboard.four_combo_score = roll.count(4) * 4 if roll.count(4) else 0
        scoreboard.five_combo_score = roll.count(5) * 5 if roll.count(5) else 0
        scoreboard.six_combo_score = roll.count(6) * 6 if roll.count(6) else 0

        for d in roll:
            if roll.count(d) == 2:
                self.two_of_kind = True

            if roll.count(d) == 3:
                self.three_of_kind = True
                scoreboard.three_of_kind_score = sum(roll)

            if roll.count(d) == 4:
                self.three_of_kind = True
                self.four_of_kind = True
                scoreboard.three_of_kind_score = sum(roll)
                scoreboard.four_of_kind_score = sum(roll)

            if self.two_of_kind and self.three_of_kind:
                self.full_house = True
                scoreboard.full_house_score = 25

            if roll.count(d) == 5:
                self.three_of_kind = True
                self.four_of_kind = True
                self.five_of_kind = True
                scoreboard.three_of_kind_score = 30
                scoreboard.four_of_kind_score = 40
                scoreboard.five_of_kind_score = 50

        if len(set(roll)) == 4 and list(sorted(set(roll))) == list(range(min(roll), max(roll) + 1)):
            self.small_straight = True
            scoreboard.three_of_kind_score = 30

        if sorted(roll) == list(range(min(roll), max(roll) + 1)):
            self.small_straight = True
            self.large_straight = True
            scoreboard.three_of_kind_score = 30
            scoreboard.four_of_kind_score = 40

        return self.__dict__

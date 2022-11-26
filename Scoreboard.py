class Scoreboard:
    def __init__(self):
        self.one_combo_score = 0
        self.two_combo_score = 0
        self.three_combo_score = 0
        self.four_combo_score = 0
        self.five_combo_score = 0
        self.six_combo_score = 0
        self.two_of_kind_score = 0
        self.three_of_kind_score = 0
        self.four_of_kind_score = 0
        self.full_house_score = 0
        self.small_straight_score = 0
        self.large_straight_score = 0
        self.five_of_kind_score = 0
        self.three_of_kind_score = 0
        self.four_of_kind_score = 0
        self.full_house_score = 0
        self.small_straight_score = 0
        self.large_straight_score = 0
        self.five_of_kind_score = 0
        self.total_score = 0

    def __setitem__(self, score, value):
        self.__dict__[score] = value

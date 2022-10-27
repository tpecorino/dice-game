class GameBoard:
    def __init__(self, roll):
        self.roll = roll


class Scoreboard:
    def __init__(self, player_id):
        self.player_id = player_id
        self.combos = []

    def update_combo(self, ):
        pass



class Combo:
    def __init__(self, combo_id, player_id, label, description, score, is_locked):
        self.combo_id = combo_id
        self.player_id = player_id
        self.label = label
        self.description = description
        self.score = score
        self.is_locked = is_locked

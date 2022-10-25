import uuid
from random import randint


class GamePiece:
    def __init__(self):
        self.id = str(uuid.uuid4())


class Die(GamePiece):
    def __init__(self, sides):
        super().__init__()
        self.sides = sides

    @staticmethod
    def roll() -> int:
        return randint(1, 6)

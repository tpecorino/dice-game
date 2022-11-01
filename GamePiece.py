import uuid
from random import randint


class GamePiece:
    def __init__(self):
        self.id = str(uuid.uuid4())


class Die(GamePiece):
    def __init__(self, sides):
        super().__init__()
        self.sides = sides

    def roll(self) -> int:
        return randint(1, self.sides)

import random

from attributes import Agile, Sneaky
from characters_2 import Character

class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
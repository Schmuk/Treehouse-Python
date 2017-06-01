import random

class Wizard:
    intelligent = True

    def __init__(self, name, intelligent=True, **kwargs):
        self.name = name
        self.intelligent = intelligent

        for key, value in kwargs.items():
            setattr(self, key, value)

    def summon_minion(self):
        return self.intelligent and bool(random.randint(0, 1))

    def teleport(self, focus):
        return self.intelligent and focus > 15


import random
class Liar(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, ** kwargs)

    def __len__(self):
        return len(self) + random.choice([3, -3])
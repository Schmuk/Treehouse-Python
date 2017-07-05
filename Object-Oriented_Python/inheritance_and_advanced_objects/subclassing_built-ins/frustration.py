import random
class Liar(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, ** kwargs)

    def __len__(self):
        fake_len = super().__len__() + random.choice([-3, 3])
        return fake_len

'''can call super() and assign result to a variable.  Can
then manipulate the value of that variable'''
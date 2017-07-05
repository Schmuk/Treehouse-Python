class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self.value) + other
        return int(self.value) + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other  # update self.value five += 1 will make self.value = 6
        return self.value

    def __sub__(self, other):
        if '.' in self.value:
            return float(self.other) - other
        return int(self.value) - other

    def __rsub__(self, other):
        return int(self.value) - other

    def __rsub__(self, other):
        return self.value - other

    def __isub__(self, other):
        self.value = self - other # update self.value (same as iadd)
        return self.value
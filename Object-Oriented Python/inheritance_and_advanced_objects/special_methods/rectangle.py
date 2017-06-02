class Rectangle:
    def __init__(self, w, l):
        self.w = w
        self.l = l

    @property
    def area(self):
        return self.w * self.l

    @property
    def perimeter(self):
        return (self.w * 2) + (self.l * 2)
class vetor_2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norma(self):
        return ((self.x ** 2) + (self.y ** 2)) ** (1/2)

    def __add__(self, other):
        return vetor_2d(self.x + other.x, self.y + other.y)


v1 = vetor_2d(3, 3)
v2 = vetor_2d(4, 5)
v3 = v1 + v2
v3.norma()

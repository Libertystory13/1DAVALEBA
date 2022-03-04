class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        print(self.x + self.y)

    def subtract(self):
        print(self.x - self.y)

    def dividing(self):
        print(self.x / self.y)

    def multiply(self):
        print(self.x * self.y)


p1 = Calculator(4, 5)
p1.sum()
p1.subtract()
p1.dividing()
p1.multiply()
class MathOperations:
    def __init__(self, num1, num2, num3=None):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def add(self):
        if self.num3 is None:
            return self.num1+self.num2
        else:
            return self.num1+self.num2+self.num3
math=MathOperations(2,3,5)
print(f"{math.add()} is the sum")

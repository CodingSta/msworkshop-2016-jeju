class Calculator(object):
    def __init__(self):
        self.base = 0
    
    def __call__(self, x, y):
        self.base += (x + y)
        return self.base

calc = Calculator()
print(calc.base)
print(calc(1, 2))   # calc.__call__(1, 2)
print(calc(1, 2))
print(calc.__call__(1, 2))


class Calculator(object):
    def __init__(self, fn):
        self.fn = fn
    
    def __call__(self, x, y):
        return self.fn(x, y)

calc = Calculator(lambda x, y: x * y)
print(calc(1, 2))

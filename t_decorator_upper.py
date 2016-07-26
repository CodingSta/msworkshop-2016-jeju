
def upper(fn):
    def wrap(x, y):
        return fn(x, y).upper()
    return wrap

@upper
def append(x, y):
    return x + y


if __name__ == '__main__':
    print(append('hello', 'world'))


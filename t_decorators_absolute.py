
def absolute_result(fn):
    wrap = lambda x, y: abs(fn(x, y))
    return wrap

def absolute_params(fn):
    wrap = lambda x, y: fn(abs(x), abs(y))
#    def wrap(x, y):
#        return fn(abs(x), abs(y))
    return wrap

@absolute_params
@absolute_result
def mysum(x, y):
    return x + y

# mysum = absolute_params(absolute_result(mysum))

@absolute_params
def mymultiply(x, y):
    return x * y

if __name__ == '__main__':
    print(mysum(2, -10))
    print(mymultiply(2, -10))
    print(mysum(2, -10))


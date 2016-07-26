import time

def memoize(fn):
    cached = {}
    def wrap(*args):
        key = args
        if key not in cached:
            cached[key] = fn(*args)
        return cached[key]
    return wrap

@memoize
def mysum(x, y, z):
    time.sleep(1)
    return x + y + z

@memoize
def mymultiply(x, y):
    time.sleep(1)
    return x * y
 
if __name__ == '__main__':
    print(mysum(1, 2, 3))
    print(mysum(1, 2, 3))
    print(mysum(1, 2, 3))
    print(mysum(2, 2, 3))
    print(mysum(2, 2, 3))
    print(mysum(2, 2, 3))
    
    print(mymultiply(2, 2))
    print(mymultiply(2, 2))
    print(mymultiply(2, 2))

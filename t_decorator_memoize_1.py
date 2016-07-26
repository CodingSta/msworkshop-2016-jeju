import time

cached_mysum = {}
cached_mymultiply = {}

def mysum(x, y):
    key = (x, y)
    if key not in cached_mysum:
        time.sleep(1)
        cached_mysum[key] = x + y
    return cached_mysum[key]
    
def mymultiply(x, y):
    key = (x, y)
    if key not in cached_mymultiply:
        time.sleep(1)
        cached_mymultiply[key] = x * y
    return cached_mymultiply[key]
 
if __name__ == '__main__':
    print(mysum(1, 2))
    print(mysum(1, 2))
    print(mysum(1, 2))
    print(mysum(2, 2))
    print(mysum(2, 2))
    print(mysum(2, 2))
    
    print(mymultiply(2, 2))
    print(mymultiply(2, 2))
    print(mymultiply(2, 2))

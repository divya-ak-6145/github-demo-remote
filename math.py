
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y       #on master


def multiply(x,y):
    return x*y           #on bug456


def divide(x,y):
    if y==0:
        return divide_by_0_error
    else:
        return x/y

#square implementation
def square(x):
    return x*x
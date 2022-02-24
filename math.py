#Add Implementation
def add(x,y):
    return x+y

#Subtract Implementation
def subtract(x,y):
    return x-y       #on master

#Multiply Implementation
def multiply(x,y):
    return x*y           #on bug456

#Divide Implementation
def divide(x,y):
    if y==0:
        return divide_by_0_error
    else:
        return x/y

#square implementation
def square(x):
    return x*x
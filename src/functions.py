"""Simple functions that can be used in Python."""

def square(n):
    """This function will take any integer/floating point value and return it's square."""
    return n**2


def cube(x): 
    
    return x**3

def lbs(k):


    return k*2.205

def kg(l):

    return l/2.205

def f(c):
   

    return (c * 9/5) + 32

def pro(x,y):


    return x * y

def div(x,y):

    if y != 0:
        return x % y
    else:
        return -999

def nsum(x,y,z):

    return x + y + z


def sq(x, y):

    if y == 'sq':

        return x**2

    else:
        return x

def slen(x):

    return  len(x)

def con(x,y):

    return x + y

def w(x):

    n = open(x, 'w')
    n.write('Hello from function')
    n.write('\n')
    n.close()


print('calling square')
print(square(5))
print(square(6))

print('calling cube')
print(cube(2))
print(cube(3))

print('calling lbs')
print(lbs(2))
print(lbs(1))

print('calling kg')
print(kg(5))
print(kg(10))

print('calling f')
print(f(32))
print(f(70))

print('calling pro')
print(pro(2, 1))
print(pro(3,4))

print('calling div')
print(div(6,3))
print(div(60, 3))

print('calling sum')
print(nsum(1,2,3))
print(nsum(10,24,3))

print('calling sq')
print(sq(2, 'sq'))
print(sq(100, 'q'))

print('calling slen')
print(slen('Hello'))
print(slen('Two'))

print('calling con')
print(con('Hello, ', 'there!'))
print(con('Scared ', 'you!'))

print('calling w')
w('Function_file1')
w('Function_file2')
 

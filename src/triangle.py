#three sides of a triangle

a = 3
b = 4
c = 5

#computing 's'
s = (a + b + c)/2 
print(s)

#computing area
t = s*(s-a)*(s-b)*(s-c) #t = area of a triangle
print(t)

t = t ** 0.5

print(t)

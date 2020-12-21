"""
This program calculates the tax of a given person
"""

x = open('in.txt')

#reading the file

for line in x:
    l = line.split()
    if l[0] == 'Name':
        n = l[1]
    elif l[0] == 'Income':
        i = int(l[1])
    elif l[0] == 'Age':
        a = int(l[1])
    elif l[0] == 'Dep':
        d = int(l[1])

x.close()

print(n, i, a, d)

#calculations

tt = (0.275*i) - (1000*d)
f = open('Tax.txt', 'w')
    
f.write(n + ' will pay $' + str(tt) + ' in taxes.')

f.close()

def min_max(a, b): # define a function that intends to sort to lists elementwise and puts greater element to first list and lesser to second

    min = []
    max = []

    for i in range(len(a)):
        if a[i] <= b[i]:
            min.append(a[i])
            max.append(b[i])
        else:
            max.append(a[i])
            min.append(b[i])

    return (min,max)

    # End of function definition!

#invoke the function

l=[]
g=[]

a=[827,2435,46674,12,543]
b=[219,92939,12233,78,5151]

l,g = min_max(a,b) # function invocation

print(l)
print(g)


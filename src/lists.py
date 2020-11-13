#!/usr/bin/python3

list1 = [1,2,3]
list2 = [2, 2, 2]
list3 = []

for i in range(len(list1)):
     list3.append(list1[i]*list2[i])

print(list3)


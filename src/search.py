# list, number, find location of number in list - if not there, print -1

def search(list,x):
    answer = -1

    for i  in range(len(list)):
        if list[i] == x:
            answer = i 

    return answer

print(search([3,45,67,82,3,5,854,2,4], 0))



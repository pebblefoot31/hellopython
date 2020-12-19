#editing
def factorial(number):
    answer = 1

    while number > 1:
        answer *= number
        number -= 1

    return answer

answer = factorial(4)

print(answer)



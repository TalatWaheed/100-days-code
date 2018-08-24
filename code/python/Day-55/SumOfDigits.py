def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

print('Minimum is:', min(100, 321, 267, 59, 40, key=sumDigit))

num = [15, 300, 2700, 821, 52, 10, 6]
print('Minimum is:', min(num, key=sumDigit))

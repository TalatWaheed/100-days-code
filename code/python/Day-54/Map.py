def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)
numbersSquare = set(result)
print(numbersSquare)

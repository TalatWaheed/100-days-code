numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, numbersTuple)

resultSet = set(result)
print(resultSet)

result = zip(numbersList, strList, numbersTuple)
resultSet = set(result)
print(resultSet)

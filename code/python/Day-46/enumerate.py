grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

print(list(enumerateGrocery))
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

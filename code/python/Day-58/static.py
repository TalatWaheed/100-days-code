class Mathematics:

    def_addNumbers(x, y):
        return x + y

Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))

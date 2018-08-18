class Person:
    age = 23
    name = "Adam"
person = Person()
print('The sex is:', getattr(person, 'sex', 'Male'))
print('The sex is:', getattr(person, 'sex'))

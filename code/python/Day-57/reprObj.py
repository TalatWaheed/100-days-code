class Person:
    name = 'Adam'

    def __repr__(self):
        return repr(self.name)

repr(Person())

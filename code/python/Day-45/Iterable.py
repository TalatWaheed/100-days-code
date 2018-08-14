numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =',numbers3)

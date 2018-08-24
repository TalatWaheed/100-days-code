randomByteArray = bytearray('ABC', 'utf-8')
print('Before updation:', randomByteArray)

mv = memoryview(randomByteArray)

mv[1] = 90
print('After updation:', randomByteArray)

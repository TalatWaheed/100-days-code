randomByteArray = bytearray('ABC', 'utf-8')

mv = memoryview(randomByteArray)

print(mv[0])

print(bytes(mv[0:2]))

print(list(mv[0:3]))

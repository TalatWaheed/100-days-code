num=int(input('Enter a number: '))

while num<=0:
    print('Error! Enter a positive number: ')
    num=int(input('Enter a number: '))
for row in range (num):
    for col in range (row):
        print('*', end='')
    print()
for i in range (num,0,-1):
    for j in range (i):
        print('*', end='')
print()

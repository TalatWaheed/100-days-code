# Python Program - Check Positive Negative and Zero

print("Enter 'x' for exit.")
num = input("Enter any number: ")
if num == 'x':
    exit()
try:
    number = int(num)
except ValueError:
    print("Try to enter a number..exiting..")
else:
    if number < 0:
    	print("It is a negative number.")
    elif number == 0:
    	print("It is a zero.")
    elif number > 0:
    	print("It is a positive number.")
    else:
    	print(number, "is strange.")

# Defining a function to reverse a string

def reverse_a_string():
   
    a_string = input("Enter a string: ")
    new_strings = []

    index = len(a_string)
    
    while index:
        index -= 1
        new_strings.append(a_string[index])

    print(''.join(new_strings))

reverse_a_string()

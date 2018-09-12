travelling = input("Are you travelling? Yes or No:")
while travelling == 'yes':
   num = int(input("Enter the number of people travelling:"))
   for num in range(1,num+1):
      name = input("Enter Details \n Name:")
      age = input("Age:")
      sex = input("Male or Female:")
      print("Details Stored \n",name)
      print(age)
      print(sex)
   print("Thank you!")
   travelling = input("Are you travelling? Yes or No:")
print("Please come back again.")

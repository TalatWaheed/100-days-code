# Program to count the number of each vowel in a string
vowels = 'aeiou'
ip_str = 'Hello, have you tried our turorial section yet?'
ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:
   if char in count:
       count[char] += 1

print(count)

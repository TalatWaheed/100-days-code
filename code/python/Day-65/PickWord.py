with open('yourfile.txt') as f:
	words = list(f)
print(random.choice(words).strip())

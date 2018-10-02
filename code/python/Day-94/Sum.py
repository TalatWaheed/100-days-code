sent = "hi people of the world"
words = sent.split(" ")

result = {}

for word in words:
    result[word] = sum(map(ord,word))

totalSum = 0

sumForSentence = [result[word] for word in words]

print ('Sum of ASCII values:')
print (' '.join(map(str, sumForSentence)))

print ('Total of all ASCII values in sentence: ',sum(sumForSentence))

def reverse_v1(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0,word)
  return " ".join(result)
def reverse_v2(x):
  y = x.split()
  return " ".join(y[::-1])
  def reverse_v3(x):
  y = x.split()
  return " ".join(reversed(y))
def reverse_v4(x):
  y = x.split()
  y.reverse()
  return " ".join(y)
test1 = input("Enter a sentence: ")
print(reverse_v1(test1))
print(reverse_v2(test1))
print(reverse_v3(test1))
print(reverse_v4(test1))

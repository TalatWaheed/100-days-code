#Program to find  if a number is divisible by 8 or not
def check(st) :
    n = len(st)
    if (n == 0) :
        return False
    if (n == 1) :
        return ((int)(st[0]) % 8 == 0)
    if (n == 2) :
        return ((int)(st[n - 2]) * 10 +
          ((int)(str[n - 1]) % 8 == 0))
 
    last = (int)(st[n - 1])
    second_last = (int)(st[n - 2])
    third_last = (int)(st[n - 3])
 
    return ((third_last*100 + second_last*10 +
                               last) % 8 == 0)
st = "76952"
if(check(st)) :
    print("Yes")
else : 
    print("No ")

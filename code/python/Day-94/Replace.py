def replaceUsingMapAndLambda(sent, a1, a2):
   
    newSent = map(lambda x: x if(x != a1 and x != a2) else a1 if x == a2 else a2, sent)
    return ''.join(newSent)

print(replaceUsingMapAndLambda("puporials toinp", "p", "t"))

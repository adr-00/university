def ordenada(l):
    if len(l) < 2:
        return True
    else:
        for i in range(len(l)- 1):
            if l[i] > l[i + 1]:
                return False
        return True
        
l = ['a', 'd', 'c']
print(ordenada(l))
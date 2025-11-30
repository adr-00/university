def ordenada(l):
    for i in range(len(l)- 1):
        if l[i] > l[i + 1]:
            print(False)
            break
        else:
            print(True)
        
l = [1, 7, 3]
ordenada(l)
def recursion(i):
    if(i==1):
        return 1
    else:
        return i*recursion(i-1)
    

print(recursion(3))

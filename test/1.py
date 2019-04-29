storedA=[]
for i in range(0,5): #how can I make the range infinity and allow user to break
    number=int(input("Enter a number: "))
    if "0" in storedA:
        break
    else:
        pass
    storedA.append(number)

lstored=len(storedA)
s=0
i=0
while i<=lstored-1:
    s=s+storedA[i]
    i=i+1
print(s)

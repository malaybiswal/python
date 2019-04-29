def solve(a0, a1, a2, b0, b1, b2):
    r0=0;r1=0;r2=0
    result=[]
    if(a0>b0):
        r0=1
    elif(a0<b0):
        r0=-1
    else:
        r0=0
    if(a1>b1):
        r1=1
    elif(a1<b1):
        r1=-1
    else:
        r1=0
    if(a2>b2):
        r2=1
    elif(a2<b2):
        r2=-1
    else:
        r2=0
    print(r0,r1,r2)
    if(r0!=0):
        result.append(r0)
    if(r1!=0):
        result.append(r1)
    if(r2!=0):
        result.append(r2)
    print(result)
    return result
a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))

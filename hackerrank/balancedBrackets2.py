import math
def match(l,m,c):
    l2=0
    match=m[l]

    if(c==1):
        l2=l+1
    else:
        l2=l2+1
        #print(m,l,m[l],"c:",c,"l2:",l2)
        #print(m[l]," compares ",m[c])
    if(match=="{" and l>0):
        if(m[c]!="}"):
            print("NO")
            return "NO"
    elif(match=="(" and l>0):
        if(m[c]!=")"):
            print("NO")
            return "NO"
    elif(match=="[" and l>0):
        if(m[c]!="]"):
            print("NO")
            return "NO"
    elif(l==0 and match=="{"):
        if(m[c]!="}"):
            print("NO")
            return "NO"
        else:
            print("YES")
            return "YES"
    elif(l==0 and match=="["):
        if(m[c]!="]"):
            print("NO")
            return "NO"
        else:
            print("YES")
            return "YES"
    elif(l==0 and match=="("):
        if(m[c]!=")"):
            print("NO")
            return "NO"
        else:
            print("YES")
            return "YES"

num=input("Eneter Number of brackets you want to match:")
num=int(num)
print(num)
str=[]
c=0
for i in range (0,num):
    s=input("Enter bracket:")
    str.insert(i,s)
for i in range(0,len(str)):
    length=len(str[i])
    if(length%2!=0):
        print("NO")
    else:
        l=math.floor(length/2)-1
        #print("MID POSITION:",l)
        m=str[i]
        c=l+1
    while(l>=0):
        result=match(l,m,c)
        if(result=="NO"):
            break
        c=c+1
        l=l-1

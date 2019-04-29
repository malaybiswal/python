import math
def is_matched(expression):
    length=len(expression)
    if(length%2!=0):
        return False
    else:
        l=math.floor(length/2)-1
#print("MID POSITION:",l)
    #m=expression[i]
    c=l+1
    while(l>=0):
        result=match(l,expression,c)
        if(result==False):
            return False
        c=c+1
        l=l-1
    #print("RESULT:",result)
    return result
def match(l,m,c):

    l2=0
    match=m[l]

    if(c==1):
        l2=l+1
        #print(m,l,m[l],"c:",c,"l2:",l2)
        #print(m[l]," compares ",m[c])
    else:
        l2=l2+1
        #print(m,l,m[l],"c:",c,"l2:",l2)
        #print(m[l]," compares ",m[c])
    if(match=="{" and l>0):
        if(m[c]!="}"):
            #print("NO")
            return False
    elif(match=="(" and l>0):
        if(m[c]!=")"):
            #print("NO")
            return False
    elif(match=="[" and l>0):
        if(m[c]!="]"):
            #print("NO")
            return False
    elif(l==0 and match=="{"):
        if(m[c]!="}"):
            #print("NO")
            return False
        else:
            #print("True")
            return True
    elif(l==0 and match=="["):
        if(m[c]!="]"):
            #print("NO")
            return False
        else:
            #print("True")
            return True
    elif(l==0 and match=="("):
        if(m[c]!=")"):
            #print("NO")
            return False
        else:
            #print("True")
            return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

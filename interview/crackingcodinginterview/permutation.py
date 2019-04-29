#Design an algorithm to print all permutations of a string. For simplicity, assume all characters are unique
def join(str,c):
    strnew=[]
    newtext=""
    strnew.append(c+str)
    i=0;length=0
    length=len(str)
    for s in str:
        i+=1
        #nextext=str[0:i]+c+str[i:length]
        #print("newtext:",newtext,"str[0:i],c,str[i:len]",str[0:i],"-",c,"-",str[i:length])
        strnew.append(str[0:i]+c+str[i:length])
    return strnew
#print(join("abc","d"))

def permString(str):
    length=len(str)
    if(len(str)<=1):
        return str
    else:

        for i in range(0,length-1):
            if i==0:
                strnew=str[0]
            print(i,strnew,str[i+1])
            return join(strnew,str[i+1])
            #return PermString(str)
print(permString("abc"))

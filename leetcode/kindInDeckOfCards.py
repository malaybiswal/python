#https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
def hasGroupsSizeX(deck):
    dict={}
    deck.sort()
    if(len(deck)<2 or len(deck)%2!=0):
        return False
    #print(deck)
    for i in deck:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict.get(i)+1
    sorted(dict.items(), key=lambda x: x[1])
    l=list(dict.values())
    print(l)
    l.sort()
    for x in l:
        print(x,len(l))
    for j in range(0,len(l)-1):
        if((l[j+1]%l[0])!=0):
            print(j,l[j+1],l[j],(l[j+1]%l[j]))
            return False
        else:
            print("---",j,l[j+1],l[j],(l[j+1]%l[j]))
    return True

d=[6,6,6,6,6,6,1,1,2,2,2,2]
print(hasGroupsSizeX(d))
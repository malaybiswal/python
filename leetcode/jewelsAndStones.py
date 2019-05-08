#https://leetcode.com/problems/jewels-and-stones/
def numJewelsInStones(J, S):
    c=0
    for x in J:
        for y in S:
            if(x==y):
                c+=1
    return c
x="zz"
y="ZZZ"
print(numJewelsInStones(x,y))
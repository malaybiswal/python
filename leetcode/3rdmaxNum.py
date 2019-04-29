#https://leetcode.com/problems/third-maximum-number/
l=[2,2,3,1]
#l=list(dict.fromkeys(l)) # to remove duplicate
l=list(set(l))
ln=len(l)
max=0
print(ln)
l.sort(reverse=True)
if(ln<3):
    max=l[0]
else:
    max=l[2]
print("MAX:",max)
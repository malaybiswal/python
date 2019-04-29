import sys

def lonely_integer(a):
    dict={}
    for i in a:
        if(len(dict)==0):
            dict[i]=1
        else:
            count=dict.get(i)

            if(count!=None):
                count+=1
                dict[i]=count
            else:
                dict[i]=1
    for key in dict:
        if(dict[key]==1):
            return key

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

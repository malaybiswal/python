"""Find from alist of numbers where each number is repeating   even number of times except one. Find that number ? """
a=[1,1,2,2,3,4,4,5,6,5,6]
a_dict={}
for i in a:
    if i not in a_dict:
        a_dict[i] =1
    else:
        a_dict[i] +=1
print(a_dict)
for i in a:
    if a_dict[i]==1:
        print (i)

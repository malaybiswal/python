num=int(input())
s=''
count=1;temp=0
while(num/2>=1):
    s=str((num%2))+s
    #print(num,"-",s)
    num=int(num/2)
    #print(num)
s=str(num)+s
#print(s)
for i in range(0,len(s)-1):
    #print(s[i],"--",s[i+1])
    if(s[i]==s[i+1]):
        if(int(s[i])==1):
            count+=1
            #print("INSIDE",count)
    elif(count>1):
        if(count>temp):
            temp=count
            count=1
        #print("INSIDE ELSE")
if(count>temp):
    print(count)
else:
    print(temp)


"""Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
Explanation

Sample Case 1:
The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2:
The binary representation of  is , so the maximum number of consecutive 's is ."""

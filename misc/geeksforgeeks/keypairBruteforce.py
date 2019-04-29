#Given an array A[] of n numbers and another number x, determine whether or not there exist two elements in A whose sum is exactly x.

def find(num_array,num,x):
    #print(num_array)
    for i in range(0,num-1):
        if(num_array[i]>x):
            print("No")
            break
        else:
            for j in range(i+1,num):
                if(num_array[i]+num_array[j]==x):
                #print("FOUND",x,"arrays items are:",num_array[i],"-",num_array[i+1])
                    print("Yes")
                    break
            else:
                continue
                
testcases=input("")
#print("Enter number of elements in array and the sum value:")
for j in range(0,int(testcases)):
    num,x= [int(x) for x in input().split()]
#n = input("num :")
    num_array=input()
#for i in range(int(num)):
    
    num_array=list(map(int,num_array.split(' ')))
    num_array.sort()
    find(num_array,num,x)
    
#print(num_array)


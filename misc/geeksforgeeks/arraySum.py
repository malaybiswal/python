#Largest Sum Contiguous Subarray
#https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

def maxSubArrySum(arr,size):
    max_so_far=0
    max_ending_here=0
    for i in range(0,size):
        max_ending_here=max_ending_here+arr[i]
        if(max_ending_here<0):
            max_ending_here=0
            print(arr[i],"--",max_so_far,"IN IF:",max_ending_here)
        elif(max_so_far<max_ending_here):
            max_so_far=max_ending_here
            print(arr[i],"--",max_so_far,"IN ELIF:",max_ending_here)
        else:
            print(arr[i],"DO NOTHING")
    return max_so_far


arr=[-2,-3,4,-1,-2,1,5,-3]
#arr=[1,2,3,4]
size=len(arr)
print(maxSubArrySum(arr,size))


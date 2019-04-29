
#https://leetcode.com/problems/contains-duplicate-ii/

def containsNearbyDuplicate(nums,k):
    diff=0
    rtype=False
    print(len(nums))
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if(nums[i]==nums[j]):
                
                diff=j-i
                print("MATCHING",i,j,diff)
                if(diff<=k):
                    rtype=True
                continue
            else:
                print("NOT MATCHING")
    return rtype
    
lst=[1,2,3,1]
f=containsNearbyDuplicate(lst,3)
print(f)

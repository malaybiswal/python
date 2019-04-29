def containsNearbyDuplicate(nums,k):
    dic={}
    for ind,key in enumerate(nums):
        if(key in dic):
            if(ind-dic[key]<=k):
                return True
        dic[key]=ind
    return False

n=[2,3,4,7,9,2]
k=6
print(containsNearbyDuplicate(n,k))
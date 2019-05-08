#https://leetcode.com/problems/min-cost-climbing-stairs/
#https://leetcode.com/problems/min-cost-climbing-stairs/discuss/276400/Forwards-Python-DP-with-explanation
def minCostClimbingStairs(costs):
    sum=0
    min1=0
    min2=0
    if(len(costs)<=0):
        return 0
    elif(len(costs)==1):
        return costs[0]
    elif(len(costs)==2):
        if(costs[0]<=costs[2]):
            return costs[0]
        else:
            return costs[1]
    else:
        for i in range (0,len(costs)-2,3):
            if(costs[i]<=costs[i+1]):
                if(len(costs)>3):
                    min1=costs[i]
                    print("1st",i)
                else:
                    min1=costs[i+1]
            elif(costs[i]>costs[i+1]):
                min1=costs[i+1]
                print("2nd",i)
            if(costs[i+1]<=costs[i+2] and len(costs)>3):
                min2=costs[i+1]
                print("3rd",i)
            elif(costs[i+1]>costs[i+2] and len(costs)>3):
                min2=costs[i+2]
                print("4th",i)
            sum=min1+min2+sum
            print(i,sum,min1,min2)
            min1=0
            min2=0
            print(i,sum,min1,min2)
        return sum




#costs=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#costs=[10, 15, 20]
costs=[0,0,1,1]
print(minCostClimbingStairs(costs))
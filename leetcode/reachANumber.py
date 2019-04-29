#https://leetcode.com/problems/reach-a-number/
def reachNumber(target):
    target = abs(target)
    if not target: 
        return 0
    step = 1
    total = 0
    while True:
        total += step            
        if total >= target and (total-target)%2 == 0:
            return step
        step += 1
    return -1

print(reachNumber(13))    


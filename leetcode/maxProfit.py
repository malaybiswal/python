#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''def maxProfit(prices):
    max=0
    globalmax=0
    print(len(prices))
    if(len(prices)<=1):
        return 0
    elif(len(prices)==2):
        if(prices[1]>prices[0]):
            return prices[1]-prices[0]
        else:
            return 0
    else:
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i] > max:
                    max= prices[j]-prices[i]
                    print("MAX:",max,j,i,prices[j],prices[i])
            if(globalmax<max):
                globalmax=max
            
    return globalmax'''

def maxProfit( prices):        
    if len(prices) == 0 or len(prices) == 1:
        return 0
    profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i]-min_price > profit:
            profit = prices[i]-min_price
        if prices[i] < min_price:
            min_price = prices[i]
    return profit 

prices=[7,1,5,3,6,4]
print(maxProfit(prices))


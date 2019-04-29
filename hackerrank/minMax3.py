lst = list(map(int, input().strip().split(' ')))
x = sum(lst)
print("sum:",x,"max:",max(lst),"min:",min(lst))
print ((x-(max(lst))), (x-(min(lst))))

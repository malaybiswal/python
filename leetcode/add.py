
def getSum(a,b) :
    if a== -b:
        return 0
    if abs(a) >abs(b):
        a,b=b,a
    while b != 0:
        carry = a&b
        a = a^b
        b = carry << 1
    return a
a=2
b=3
print(getSum(a,b))
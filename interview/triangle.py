def calculate(a,b,c):
    if(a==b and a==c and b==c):
        return ("equilateral")
    elif(a==b or a==c or b==c):
        return("isosceles")
    else:
        return("scalene")
a=input("enter side1 of triangle:")
b=input("enter side2 of triangle:")
c=input("enter side3 of triangle:")
print(calculate(a,b,c))

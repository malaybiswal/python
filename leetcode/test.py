


def judgeSquareSum(c):
    flag=False
    num=0
    num1=0
    num2=0
    for i in range(1,c+1):
        if(i*i>c):
            num=i
            print("I:",i)
            break
    
    #print(num)
    for j in range(0,num+1):
        for k in range(0,num+1):
            if(((j*j)+(k*k))==c):
                #print("INSIDE j,k,n matching",j,k,n)
                flag=True
                num1=j
                num2=k
                break
    print(flag,num1,num2)
    print(flag)
    return;

judgeSquareSum(100000000)

def exponential(base,exp):
    if(exp==0):
        return 1
    else:
        base=base*exponential(base,exp-1)
        return base
print(exponential(2,998))

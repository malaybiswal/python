def almost_palindromes(str):
    strReverse=str[::-1]
    count=0;j=0
    for s in str:
        if(s==strReverse[j]):
            count=count
        else:
            count=count+1
        j+=1
    return count

i=almost_palindromes("cuat")
print(i)

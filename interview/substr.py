def substr(str,str2):
    if(str2 in str):
        return "FOUND"
    else:
        return "Not FOUND"
print(substr("abcdef","de"))

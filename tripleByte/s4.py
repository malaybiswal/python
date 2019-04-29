def ascii_deletion_distance(str1, str2):
    sum=0
    for s1 in str1:
        position=str2.find(s1)
        if(position>=0):

            str2=str2.replace(str2[position],'',1)
            print("in if:",str2)
        else:
            sum=sum+ord(s1)
    print(str2)
    for i in str2:
        sum=sum+ord(i)
    return sum
#i=ascii_deletion_distance("thought", "sloughs")
#i=ascii_deletion_distance("at", "cat")
i=ascii_deletion_distance("boat", "got")
print(i)

i=0
dict={}
with open("/Users/mala0858/Downloads/misc.txt","r") as f:
    for line in f:
        i+=1
        lines=line.split()
        #print(i,lines[0])
        if(i==1):
            dict[lines[0]]=1
        else:
            #count=dict[lines[0]]
            try:

                dict[lines[0]]=dict[lines[0]]+1
            except:
                dict[lines[0]]=1


with open("/Users/mala0858/Downloads/misc1.txt","w") as f:
    for k,v in dict.items():
        k=k+" "+str(v)
        f.write(k)
        f.write("\n")
        print(k)

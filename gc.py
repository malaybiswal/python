file = open("/Users/mala0858/malay/rackspace/onewiki/2018/DBMigrationProdTest/test-1/2018-03-10_03-37-31-gc.log.0","r")
t=[]
tm=0.0;count=0;first=0.0
for line in file:
    text=line.split("secs")
    #text.trim()
    t=text[0].split(",")
    #print("----",text[0])
    tm1=text[0].split(" ")
    if(count==0):
        first= tm1[0]
    l=len(t)
    #print(l,t[l-1])
    tm=tm+float(t[l-1])
    count+=1
totaltime=float(tm1[0][:-1])-float(first[:-1])

#print(totaltime)
print("TOTAL TIME SPENT IN GC:",tm,"SECONDS - AVg Time spent in GC:",float(tm/count),"SECONDS - #OF GC:",count)
throughput=(1-(tm/totaltime))*100
print("THROUGHPUT:",throughput)


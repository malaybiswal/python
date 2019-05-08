
# read the string filename . VISA interview question. Read file and parse it, out file will have hostnames and count of occurrences
filename = input()
filename1="/Users/mala0858/malay/python/leetcode/"+filename
outfile="/Users/mala0858/malay/python/leetcode/records_"+filename
fr=open(filename1,"r")
host=""
hostlist=[]
hostdict={}
for line in fr:
    lines=line.split()
    host=lines[0]
    hostlist.append(host)
fr.close()
for f in hostlist:
    if f not in hostdict:
        hostdict[f]=1
    else:
        hostdict[f]+=1

fw=open(outfile,"w")
for key,val in hostdict.items():
    fw.write(key)
    fw.write(" ")
    fw.write(str(val))
    fw.write("\n")
fw.close()


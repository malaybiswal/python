#!/usr/local/bin/python3


fin = open('/Users/mala0858/malay/python/PythonIIData/trees.dat','r')
trees=[]
totalheight=0;
numtrees=0;
avgheightoftrees=0;
heightoftallesttree=0;
heightofshortesttree=0;
x= fin.readlines()
for str in x:
	numtrees+=1
	trees.append(str)
	totalheight=totalheight+float(str)


avgheightoftrees = totalheight/numtrees
heightoftallesttree=max(trees)
heightofshortesttree=min(trees)

print(numtrees,avgheightoftrees,heightoftallesttree,heightofshortesttree)

#pct=(float)((count/total)*100)
#print('Total letters: {0:,d}'.format(total))
#print(count)
#print(pct)
#print('{0:.2%} of all the letter are e\'s'.format(pct/100))
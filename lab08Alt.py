fin=open('/Users/mala0858/malay/python/PythonIIData/gdp.txt', 'r')
x=fin.readlines()
total=0
gdp={}

for i in x:
	print(i,'----------')
	i=''.join(i)
	
	str=i.split(',')
	#print('--',str[0],str[1],''.join(str[2].splitlines()),'**')
	print(total)
	#gdp[total][0]=str[0]
	#gdp[total][1]=str[1]
	#gdp[total][2]=''.join(str[2].splitlines())
	percapita=float(''.join(str[2].splitlines()))/float(str[1])
	#print(percapita)
	total+=1
	gdp[str[0]]=percapita
#print(total,len(gdp))

sort=reversed(sorted(zip(gdp.values(),gdp.keys())))
for i in sort:
	print(i)
fin.close()
print('-----------------------')

input('\n\r Press ENTER to continue.\n\r')
from string import punctuation

fin=open('/Users/mala0858/malay/python/PythonIIData/split.txt', 'r')
x=fin.readlines()
str='.'.join(x)
str.upper()
words=str.split()
print('total number of words:',len(words))
s=set()
s=set(words)
print(s)
print(len(s))
#l=list()
print('-----------------------')
l=list(s)
l.sort()
print(l)
#for i in x:
#	if(i.isalpha):

#print(list(sort))
fin.close()



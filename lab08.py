fin=open('/Users/mala0858/malay/python/PythonIIData/gdp.txt', 'r')
x=fin.readlines()
total=0
gdp=[]
for i in range(38):
	gdp.append([0,0,0])
print(gdp)
for i in x:
	print(i,'----------')
	i=''.join(i)
	
	str=i.split(',')
	print('--',str[0],str[1],''.join(str[2].splitlines()),'**')
	print(total)
	gdp[total][0]=str[0]
	gdp[total][1]=str[1]
	gdp[total][2]=''.join(str[2].splitlines())
	total+=1
	print(gdp)
print(total,len(gdp))

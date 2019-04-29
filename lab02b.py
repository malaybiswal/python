#!/usr/local/bin/python3

total=0
count=0;
perccount=0;
perctot=0;
fin = open('/Users/mala0858/malay/python/PythonIIData/tmpprecip2012.dat','r')

x= fin.readlines()

for str in x:
	total=total+1
	#print(str)
	month=str[0:2]
	day=str[2:4]
	year=str[4:8]
	perc=str[8:13]
	perctot=perctot+float(perc)
	hightemp=str[13:16]
	#print(month)
	#print(day)
	#print(year)
	#print(perc)
	#print(hightemp)
	if((perc[0]=='0') and (perc[1]=='0') and (perc[3]=='0') and (perc[4]=='0') ):
		count=count+1;
	else:
		perccount=perccount+1

#print('------------')
#print(total)
#print(count)
#print(perccount)
#print(perctot)

print('Total pecripitation days: {0:,d}'.format(perccount))
print('Total Percipitation: {0:.2f}'.format(perctot))
fin.close()

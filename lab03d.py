#!/usr/local/bin/python3
import random
dobct=0
total=0
DOB=[]
def dob():
	dobNumbers=random.randint(1,365) 
	return dobNumbers
def dobfun():
	for i in range(0,23,1):
		num=dob()
		#print(num)
		DOB.append(num)



	#print(num,DOB)
#count=[]
#print(DOB)
#print(DOB[1])
#k=0
for j in range(1,10001,1):
	dobfun()
	print(DOB)
	for i in DOB:
		dobct=DOB.count(i)
		if(dobct>1):
			total=total+1
			break
	DOB=[]
	
print('total number of people having duplictae dates  {0:3d}'.format(total))

#pct=(float)((count/total)*100)
#print('Total letters: {0:,d}'.format(total))
#print(count)
#print(pct)
#print('{0:.2%} of all the letter are e\'s'.format(pct/100))
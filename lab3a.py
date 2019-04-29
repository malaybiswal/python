#!/usr/local/bin/python3
def diceroll():
		roll = (randint(1,6))+(randint(1,6))
		return roll

from random import randint
rollcounts = 11*[0]
pctrollcnt = 11*[0]
for i in range(1,100000,1):
	roll = diceroll()
	rollcounts[roll-2]+=1

for j in range(0,11,1):
	pctrollcnt[j] = (float)(rollcounts[j]/100000)*100
	print(j+2,pctrollcnt[j],rollcounts[j])

#print ('Now Balance= ${0:,d}'.format(bal))
			





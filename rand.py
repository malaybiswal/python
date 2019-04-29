#!/usr/local/bin/python3
def diceroll():
		roll = (randint(1,6))+(randint(1,6))
		return roll

def firstroll(roll):
		if roll == 7:
			return 1
		elif roll == 11:
			return 1
		elif roll == 2:
			return 0
		elif roll == 3:
			return 0
		elif roll == 12:
			return 0
		else:
			return 2

def nextroll(roll):
		if roll == 7:
			return 0
		else:
			return 1

from random import randint
bal=100
print ('Beginning Balance= ${0:,d}'.format(bal))
for i in range(1,100):
	roll = diceroll()
	if i==1:
		num = firstroll(roll)
		if num == 1:
			bal=bal+10
			print(roll)
			print ('Now Balance= ${0:,d}'.format(bal))
		elif num==0:
			bal=bal;
			print(roll)
			print ('Now Balance= ${0:,d}'.format(bal))
			break
		elif num==2:
			bal=bal
			print(roll)
			print ('Now Balance= ${0:,d}'.format(bal))

	else:
		num = nextroll(roll)
		if num ==1:
			bal = bal+10
			print(roll)
			print ('Now Balance= ${0:,d}'.format(bal))
		else:
			bal = bal-10;
			print(roll)
			print ('Now Balance= ${0:,d}'.format(bal))
			break





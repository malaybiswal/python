#!/usr/local/bin/python3

total=0
count=0;
perccount=0;
perctot=0;
fin = open('/Users/mala0858/malay/python/PythonIIData/tmpprecip2012.dat','r')
cnt=[0,0,0,0,0,0,0,0,0,0,0,0]
total=[0,0,0,0,0,0,0,0,0,0,0,0]
x= fin.readlines()
temp=[]
for i in range(13):
	temp.append([0,0,0,1000])
print(temp)

for str in x:
	#total=total+1
	#print(str)
	month=int(str[0:2])
	day=int(str[2:4])
	year=int(str[4:8])
	perc=float(str[8:13])
	#perctot=perctot+float(perc)
	hightemp=int(str[13:16])
	#print(month)
	#print(day)
	#print(year)
	#print(perc)
	#print(hightemp)
	if(month==1):
		cnt[0]+=1
		temp[1][0]=1
		total[0]=total[0]+hightemp
		temp[1][1]=float(total[0]/cnt[0])
		if(temp[1][2]<hightemp):
			temp[1][2]=hightemp
		if(temp[1][3]>hightemp):
			temp[1][3]=hightemp
	if(month==2):
		cnt[1]+=1
		temp[2][0]=2
		total[1]=total[1]+hightemp
		temp[2][1]=float(total[1]/cnt[1])
		if(temp[2][2]<hightemp):
			temp[2][2]=hightemp
		if(temp[2][3]>hightemp):
			temp[2][3]=hightemp
	if(month==3):
		cnt[2]+=1
		temp[3][0]=3
		total[2]=total[2]+hightemp
		temp[3][1]=float(total[2]/cnt[2])
		if(temp[3][2]<hightemp):
			temp[3][2]=hightemp
		if(temp[3][3]>hightemp):
			temp[3][3]=hightemp
	if(month==4):
		cnt[3]+=1
		temp[4][0]=4
		total[3]=total[3]+hightemp
		temp[4][1]=float(total[3]/cnt[3])
		if(temp[4][2]<hightemp):
			temp[4][2]=hightemp
		if(temp[4][3]>hightemp):
			temp[4][3]=hightemp
	if(month==5):
		cnt[4]+=1
		temp[5][0]=5
		total[4]=total[4]+hightemp
		temp[5][1]=total[4]/cnt[4]
		if(temp[5][2]<hightemp):
			temp[5][2]=hightemp
		if(temp[5][3]>hightemp):
			temp[5][3]=hightemp
	if(month==6):
		cnt[5]+=1
		temp[6][0]=6
		total[5]=total[5]+hightemp
		temp[6][1]=float(total[5]/cnt[5])
		if(temp[6][2]<hightemp):
			temp[6][2]=hightemp
		if(temp[6][3]>hightemp):
			temp[6][3]=hightemp
	if(month==7):
		cnt[6]+=1
		temp[7][0]=7
		total[6]=total[6]+hightemp
		temp[7][1]=float(total[6]/cnt[6])
		if(temp[7][2]<hightemp):
			temp[7][2]=hightemp
		if(temp[7][3]>hightemp):
			temp[7][3]=hightemp
	if(month==8):
		cnt[7]+=1
		temp[8][0]=8
		total[7]=total[7]+hightemp
		temp[8][1]=float(total[7]/cnt[7])
		if(temp[8][2]<hightemp):
			temp[8][2]=hightemp
		if(temp[8][3]>hightemp):
			temp[8][3]=hightemp
	if(month==9):
		cnt[8]+=1
		temp[9][0]=9
		total[8]=total[8]+hightemp
		temp[9][1]=float(total[8]/cnt[8])
		if(temp[9][2]<hightemp):
			temp[9][2]=hightemp
		if(temp[9][3]>hightemp):
			temp[9][3]=hightemp
	if(month==10):
		cnt[9]+=1
		temp[10][0]=10
		total[9]=total[9]+hightemp
		temp[10][1]=float(total[9]/cnt[9])
		if(temp[10][2]<hightemp):
			temp[10][2]=hightemp
		if(temp[10][3]>hightemp):
			temp[10][3]=hightemp
	if(month==11):
		cnt[10]+=1
		temp[11][0]=11
		total[10]=total[10]+hightemp
		temp[11][1]=float(total[10]/cnt[10])
		if(temp[11][2]<hightemp):
			temp[11][2]=hightemp
		if(temp[11][3]>hightemp):
			temp[11][3]=hightemp

	if(month==12):
		cnt[11]+=1
		temp[12][0]=12
		total[11]=total[11]+hightemp
		temp[12][1]=float(total[11]/cnt[11])
		if(temp[12][2]<hightemp):
			temp[12][2]=hightemp
		if(temp[12][3]>hightemp):
			temp[12][3]=hightemp
print('---------------------------')
cnt1=0
for l,l1,l2,l3 in temp:
	cnt1+=1
	if(cnt1>1):
		print('{0:3d}   '.format(l),    '{0:.1f}    '.format(l1),    '{0:3d}     '.format(l2),    l3)
#print('------------')
#print(total)
#print(count)
#print(perccount)
#print(perctot)
#print(cnt[0],cnt[1])
#print('Total pecripitation days: {0:,d}'.format(perccount))
#print('Total Percipitation: {0:.2f}'.format(perctot))
fin.close()
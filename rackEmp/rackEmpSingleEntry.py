#import urllib2
# started with 800,000 ID
import datetime
from re import sub
import re
from decimal import Decimal
import pymysql
import ssl
import sys
import traceback
import time

def insert(name):
    j=0
    try:
    	id=int(sys.argv[1])
    except:
    	id=1234
    url="https://finder.rackspace.net/index.php?q="
    url1=url+name
    i=0
    try:
    	from urllib.request import urlopen
    except ImportError:
    	from urllib2 import urlopen
    #url=url1+str(id)
    conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='rackemp',use_unicode=True, charset="utf8")
    sql="""INSERT INTO rackemp(name,designation,location,phone,ext,mobile,hiredate,username,boss) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cur = conn.cursor()
    count=0;name='';designation='';location='';phone='';ext='';mobile='';hiredate='';username='';boss=''
    context = ssl._create_unverified_context()
    #page = urllib2.urlopen(url)
    page=urlopen(url1,context=context)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page)
    all_tab=soup.find('table')
    datasets = []
    print('-----------',all_tab)
    if(all_tab is None):
        print("all_tab has no data")
    else:

        for row in all_tab.find_all("tr")[1:]:
            i+=1
            dataset =  (td.get_text() for td in row.find_all("td"))
            datasets.append("###".join(dataset))
        for data in datasets:
            parsestring = data.split("###")
            name=parsestring[0]

            designation=parsestring[1]
            location=parsestring[2]
            phone=parsestring[3]
            if(len(phone)<=1):
                phone='000-000-0000'
            ext=parsestring[4]
            if(len(ext)<=1):
                ext='000-000-0000'
            mobile=parsestring[5]
            if(len(mobile)<=1):
                mobile='000-000-0000'

            hiredate=parsestring[6]
            try:
                hiredate=datetime.datetime.strptime(hiredate, '%m/%d/%Y')
            except ValueError:
                hiredate='1000-01-01 00:00:00'
            username=parsestring[7]
            boss=parsestring[8]
            try:
                cur.execute(sql,(name,designation,location,phone,ext,mobile,hiredate,username,boss))

            except:
                j+=1
                print("DB ERROR!!!!!!!!!!!!!!!!!!")
                print(traceback.format_exc())
                #print('ERROR: %sn' % str(err))
                print(name,':',designation,':',location,':',phone,':',ext,':',mobile,':',hiredate,':',boss,'---',len(phone))
    conn.commit()
    cur.close()
    conn.close()
    print(i,'-',i-j)

def find_word(text, search):

   result = re.findall('\\b'+search+'\\b', text, flags=re.IGNORECASE)
   #print('RESULT',result,len(result))
   if len(result)>0:
      return True
      print('RETURNING TRUE','********************')
   else:
      return False
      #print('RETURNING FALSE','********************')


print ('Number of arguments:', len(sys.argv), 'arguments.')

start = time.time()
#name='car'
name='bra'
insert(name)

end = time.time()
print("TOTAL TIME TAKEN:",end - start)


#pwsource varchar(30),  , educationmin varchar(100),,trainingrequired varchar(10),alteducation varchar(100),

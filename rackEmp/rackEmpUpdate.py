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
def getdata(url1,username1,conn):
    i=0
    try:
    	from urllib.request import urlopen
    except ImportError:
    	from urllib2 import urlopen
    #conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='rackemp',use_unicode=True, charset="utf8")
    cur = conn.cursor()
    updatesql="""update rackemp set left_t=%s where binary trim(username)=%s and left_t is NULL"""
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    context = ssl._create_unverified_context()
    #page = urllib2.urlopen(url)
    print(url1)
    page=urlopen(url1,context=context)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page)
    all_tab=soup.find('table')
    datasets = []
    print('-----------',all_tab)

    if(all_tab is None):
        print('INSIDE UPDATE')
        try:
            print('***************',(st,username1))
            cur.execute(updatesql,(st,username1))
            conn.commit()
        except:
            print("DB ERROR while UPDATING...")
            print(traceback.format_exc())
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
            #Call check database to find username, if not update left_t
            print(username,boss,'--------------')
        print("NO ACTION AS USERNAME EXISTS...",username1)


    cur.close()


start = time.time()
url="https://finder.rackspace.net/index.php?q="
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='rackemp',use_unicode=True, charset="utf8")
#selectsql= """select username from rackemp where left_t is  NULL and designation not like 'Service Account%' """
selectsql= """select username from rackemp where left_t is  NULL and designation not like 'Service Account%' and username not like '%bjor2636%'"""
#selectsql= """select username from rackemp where left_t is  NULL and designation not like 'Service Account%' and trim(username) REGEXP '^[m-z].*$'"""
cur1 = conn.cursor(pymysql.cursors.DictCursor)

try:
    count=0

    cur1.execute(selectsql)
    #data=cur1.fetchall()
    print(bool(cur1),cur1)
    for row in cur1:
        count+=1
        r=row['username'].strip()
        print('USERNAME:',r+'NOTTHESE')
        #url=url+row['username'].encode('utf-8')
        if(r==' björ2636'):
            print('THIS FUCKER...',r)
            continue
        url=url+r
        getdata(url,r,conn)
        url="https://finder.rackspace.net/index.php?q="
        print('In Loop',count)

except:
    print("DB ERROR!!!!!!!!!!!!!!!!!!")
    print(traceback.format_exc())
cur1.close()
conn.close()
end = time.time()
print("TOTAL TIME TAKEN:",end - start)

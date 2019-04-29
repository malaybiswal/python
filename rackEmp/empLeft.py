import datetime
from re import sub
import re
from decimal import Decimal
import pymysql
import ssl
import sys
import traceback
import time

def lookup(e):
    url="https://finder.rackspace.net/index.php?q="
    url=url+e.strip()
    #print(url)
    try:
    	from urllib.request import urlopen
    except ImportError:
    	from urllib2 import urlopen
    context = ssl._create_unverified_context()
    page=urlopen(url,context=context)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page)
    all_tab=soup.find('table')
    datasets = []
    #print('-----------',all_tab)

    if(all_tab is None):
        print(e)
emp=""
with open('file.txt') as fp:
    for line in fp:
        line=line.strip()
        #emp="'"+line+"'"+","+emp
        emp=line+","+emp
emp=emp[:-1]
print (emp)
fp.close()
emps=emp.split(",")
for  e in emps:
    lookup(e)

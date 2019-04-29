#This program get GC details each day along with sequence id which is needed in 2nd program and inserts record into icertportal table
import datetime
from re import sub
import re
from decimal import Decimal
import pymysql
import ssl
import sys
import traceback
import datetime
from datetime import date, timedelta






#url ="http://indiawater.gov.in/IMISWeb/DataEntry/HabitationDirectory/Reports/Rep_DirectoryList.aspx?Condition=P50votMRqBU%3D&id=K7q1T96Sg9c%3D&StateName=tOqmLIPFAic%3D&DistrictName=4nlwDWnpU4w%3D&level=3SF6adRVTpM%3D&sublevel=zf5afxWBEDk%3D"

import libxml2
doc = libxml2.parseFile('/Users/mala0858/Downloads/baripadaVillages')
for url in doc.xpathEval('//@Cell'):
  print (url.content)

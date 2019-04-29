import requests
import datetime
from datetime import date, timedelta
import json
import csv
import sys
import urllib.request

#reload(sys)
#from imp import reload
import imp
#imp.reload(sys)
#reload(sys)
#sys.setdefaultencoding('utf-8')
for x in range(1,2):
    da = date.today() - timedelta(days=x)
    url ="https://icert.doleta.gov/index.cfm?event=ehLCJRExternal.dspQuickCertSearchGridData&&startSearch=1&case_number=&employer_business_name=&visa_class_id=6&state_id=all&location_range=10&location_zipcode=&job_title=&naic_code=&create_date=undefined&post_end_date=undefined&h1b_data_series=ALL&start_date_from="+da.strftime("%m/%d/%Y")+"&start_date_to="+(da-timedelta(days=1)).strftime("%m/%d/%Y")+"&end_date_from=mm/dd/yyyy&end_date_to=mm/dd/yyyy&nd=1464942893598&page=2&rows=1000&sidx=create_date&sord=desc&nd=1464942948365&_search=false"
    fname = "icert-"+da.strftime('%Y-%m-%d')+".json"
    ffname = "icert-final.json"
    print ("Processed: icert-"+da.strftime('%Y-%m-%d')+".json File.")
    #r = requests.get(url)
    #r=r.decode('utf-8')
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    r= json.loads(r.decode('utf-8'))
    re = r.content.replace(",",", ").replace(":",": ")
    f = open(fname,'w')
    f.write(re)
    f.close()
    ff = open(ffname,'a')
    ff.write(re+"\n")
    ff.close()
infile = open("bq-input.csv","w")
with open("icert-final.json","r") as ifile:
    for line in ifile:
        x = json.loads(line)
        y = x['ROWS']
        if len(x['ROWS']) !=0:
            for i in y:
                approval_date_s = str(i[2])
                approval_date = approval_date_s[6:] + "-" + approval_date_s[:2] + "-" + approval_date_s[3:5] + " 00:00:00"
                case_id = str(i[1])
                case_year = "20" + case_id[2:-9]
                case_day = case_id[4:7]
                case_date = datetime.datetime(int(case_year),1,1) + datetime.timedelta(int(case_day)-1)
                infile.write(str(i[0])+"|"+str(i[1])+"|"+approval_date+"|"+str(i[5])+"|"+str(i[8])+"|"+str(i[9])+"|"+str(case_date))
                infile.write('\n')
infile.close()

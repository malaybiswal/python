with open("log.txt") as f:
    content=f.readlines()
    content = [x.strip() for x in content]
text={}
for s in content:
    str=s.split(" ")
    job=str[4].strip().split("[")[0]
    user=str[5].strip()[1:len(str[5])-1]
    command=str[6].strip()
    t=job+" "+user+" "+command
    try:
        if(text[t]>=1):
            text[t]=text[t]+1
    except:
        text[t]=1
for t in text:
    print(t,text[t])


"""You are given a 2G syslog file with each line in the format:

Month Day hh:mm:ss hostname service[PID]: (userid) command a b c d e f ...

Where Day, PID is an integer and rest of the fields are alpha-numeric strings.

For each service and user, the command string may occur multiple times in the syslog file. We need to find the number of occurrences of a command for each (service, user, command) combination.

Write a tool that will prepare a table with each line containing:
service userid command number-of-times-the-command-occurs-in-syslog

For example, for input:
Dec 10 07:17:01 ip-10-198-43-75 CRON[19220]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Dec 10 08:17:01 ip-10-198-43-75 CRON[30306]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Dec 10 09:17:01 ip-10-198-43-75 CRON[9098]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Dec 10 10:17:01 ip-10-198-43-75 CRON[20128]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Dec 10 11:17:01 ip-10-198-43-75 CRON[31240]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Dec 10 12:17:01 ip-10-198-43-75 CRON[9881]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Dec 10 13:17:01 ip-10-198-43-75 CRON[20902]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Dec 10 14:17:01 ip-10-198-43-75 CRON[31972]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

The output would be:
CRON  root  CMD 8"""

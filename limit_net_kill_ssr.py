#coding=utf-8

limit_total=0# limit_total 上传+下载的流量限制，单位GB，如果不限制就是0，如果限制1T就是1024
limit_in=0# limit_in 下载的流量限制，单位GB，如果不限制就是0，如果限制1T就是1024
limit_out=1# limit_out 上传的流量限制，单位GB，如果不限制就是0，如果限制1T就是1024
sleep=1#多久检查一次，单位是秒
url='https://tgbot.lbyczf.com/sendMessage/cnbe1mjnqnx79p'
message={'text':'sgp2 run out of bandwidth'}


import os
import time
import request
NET_IN = 0
NET_OUT = 0

while True:
	vnstat=os.popen('vnstat --dumpdb').readlines()
	for line in vnstat:
		if line[0:4] == "m;0;":
			mdata=line.split(";")
			NET_IN=int(mdata[3])/1024
			NET_OUT=int(mdata[4])/1024
            print(NET_OUT)
			break

	#killssr="`ps aux|grep server.py|awk '{print \"kill \"$2}'`"
	#killssr="'curl -d \"text=sgp2 run out of bandwidth\" -X POST https://tgbot.lbyczf.com/sendMessage/cnbe1mjnqnx79p -s > /dev/null '"
	if (limit_total != 0 and (NET_IN+NET_OUT)>=limit_total):
		requests.post(url, data=message)
		break
	elif (limit_in != 0 and NET_IN>=limit_in):
		requests.post(url, data=message)
		break
        elif (limit_out != 0): #and NET_OUT>=limit_out):
		requests.post(url, data=message)
		break

	time.sleep(sleep)
	

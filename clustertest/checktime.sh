#!/bin/bash
export PATH=$PATH:/usr/local/bin
# NOTE: cds02 is a windows machine and it has to be run manually
# set the time for all analytic engine server, do NOT set time to 0/5 min nor setting it while at 0/5 min
dt1="2016-08-15 14:59:00"

logfile="/workspace/ws03/IData/Users/Daniel/Support/clustertest/scheduler.sh.log"
t1=`date --date="$dt1" +%s`
dt2=`date +%Y-%m-%d\ %H:%M:%S`
t2=`date --date="$dt2" +%s`
let "secDiff=$t1-$t2"
# only update within 300 sec or 5 min range for cron job to run
if [ "$secDiff" -gt 280 ] || [ "$secDiff" -lt -280 ]; then
	echo "$HOSTNAME: $dt2 Not scheduled because time diff is: $secDiff" >> $logfile
	exit
fi
echo "$HOSTNAME: $dt2 running because time diff is: $secDiff" >> $logfile

/bin/bash python /workspace/ws03/IData/Users/Daniel/Support/clustertest/test1.py

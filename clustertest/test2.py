fhand=open('IData/Users/pipelinerun/jobs/20160729_PID_TestJobs.osreg.txt')
count=0
for line in fhand:
	line=line.rstrip()
	if line.startswith('['):
		print line, count
	count+=1
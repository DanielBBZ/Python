import re
file = open('IData/Users/pipelinerun/jobs/20160729_PID_TestJobs.osreg.txt', 'r')
for line in file.readlines():
	if re.search('\S', line):
		print line,
file.close()
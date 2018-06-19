
#merge file of head.txt, sample.txt,and template.osreg and save as machine1.osreg
filenames = ['/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/head.txt','/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/sample1.txt', '/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/template02.osreg']
with open('/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/machine1.osreg', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())


filenames = ['/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/head.txt','/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/sample2.txt', '/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/template03.osreg']
with open('/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/machine2.osreg', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())
			
			
filenames = ['/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/head.txt','/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/sample3.txt', '/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/template04.osreg']
with open('/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/machine3.osreg', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())
			
			
			
filenames = ['/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/head.txt','/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/sample1.txt', '/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/template.osreg']
with open('/workspace/ws03/IData/Users/pipelinerun/jobs/_jobtemplate/machine4.osreg', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())
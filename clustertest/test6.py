from itertools import islice
with open("/workspace/ws03/IData//Users/pipelinerun/jobs/_jobtemplate/20160803_TestFileList.txt", "r") as myfile:
	head = list(islice(myfile, 2))
	sample = list(myfile)

with open("/workspace/ws03/IData//Users/pipelinerun/jobs/_jobtemplate/head.txt", "w") as f2:
	for item in head:
		f2.write(item)
		
with open("/workspace/ws03/IData//Users/pipelinerun/jobs/_jobtemplate/sample.txt", "w") as f2:
	for item in sample:
		f2.write(item)
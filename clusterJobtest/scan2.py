import glob, os
os.chdir("/IData/Users/pipelinerun/jobs/_jobtemplate/scan/")
for file in glob.glob("*.txt"):
	print(file)
try:
	myfile =open(file, 'r')
except: 
	print('There is no text file!')
	exit()
	

print 'file for registration is found'
print myfile
#step 1: separate filelist content into 2 files, head file and sample file 
from itertools import islice
#with open("IData/Users/pipelinerun/jobs/_jobtemplate/20160803_TestFileList.txt", "r") as myfile:
head = list(islice(myfile, 2))
sample = list(myfile)

with open("IData/Users/pipelinerun/jobs/_jobtemplate/head.txt", "w") as fi1:
	for item in head:
		fi1.write(item)
		
with open("IData/Users/pipelinerun/jobs/_jobtemplate/sample.txt", "w") as fi2:
	for item in sample:
		fi2.write(item)


#step 2: define sample numbers for each machine, separate these samples into each file
with open("IData/Users/pipelinerun/jobs/_jobtemplate/sample.txt") as f1:
	lines=f1.readlines()
	count = len(lines)
	print 'Total Sample Number is', count

#sample number ratio: 2:2:2:1
#all_list = range(count+1)[1:]
#list1 = [x for x in all_list if (x%7==1) or (x%7==2) ]
#list2 = [x for x in all_list if (x%7==3) or (x%7==4) ]
#list3 = [x for x in all_list if (x%7==5) or (x%7==6) ]
#list4 = [x for x in all_list if (x%7==7) or (x%7==0) ]

#sample number ratio: 2:2:3:1
all_list = range(count+1)[1:]
list1 = [x for x in all_list if (x%8==1) or (x%8==2) ]
list2 = [x for x in all_list if (x%8==3) or (x%8==4) ]
list3 = [x for x in all_list if (x%8==5) or (x%8==6) or (x%8==7)]
list4 = [x for x in all_list if (x%8==8) or (x%8==0) ]

print 'machine1 (CDS02) sample number', list1
print 'machine2 (CDS03) sample number', list2
print 'machine3 (CDS04) sample number', list3
print 'machine4 (Test-03) sample number', list4

with open("IData/Users/pipelinerun/jobs/_jobtemplate/sample1.txt", "w") as f2:
	with open("IData/Users/pipelinerun/jobs/_jobtemplate/sample2.txt", "w") as f3:
		with open("IData/Users/pipelinerun/jobs/_jobtemplate/sample3.txt", "w") as f4:
			with open("IData/Users/pipelinerun/jobs/_jobtemplate/sample4.txt", "w") as f5:
				for item in list1:
					f2.write(lines[item-1])
				for item in list2:
					f3.write(lines[item-1])
				for item in list3:
					f4.write(lines[item-1])
				for item in list4:
					f5.write(lines[item-1])


#Step 3: Merge files to be a whole registration file
#merge file of head.txt, sample.txt,and template.osreg and save as machine1.osreg
#File path for this machine: IData/Users/pipelinerun/servers/cds02.omicsoft.com/[Instruction]
filenames = ['IData/Users/pipelinerun/jobs/_jobtemplate/head.txt','IData/Users/pipelinerun/jobs/_jobtemplate/sample1.txt', 'IData/Users/pipelinerun/jobs/_jobtemplate/template02.osreg']
with open('IData/Users/pipelinerun/jobs/_jobtemplate/machine1.osreg', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())

#File path for this machine: IData/Users/pipelinerun/servers/cds03.omicsoft.com/[Instruction]
filenames = ['IData/Users/pipelinerun/jobs/_jobtemplate/head.txt','IData/Users/pipelinerun/jobs/_jobtemplate/sample2.txt', 'IData/Users/pipelinerun/jobs/_jobtemplate/template03.osreg']
with open('IData/Users/pipelinerun/jobs/_jobtemplate/machine2.osreg', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())

#File path for this machine: IData/Users/pipelinerun/servers/cds04.omicsoft.com/[Instruction]
filenames = ['IData/Users/pipelinerun/jobs/_jobtemplate/head.txt','IData/Users/pipelinerun/jobs/_jobtemplate/sample3.txt', 'IData/Users/pipelinerun/jobs/_jobtemplate/template04.osreg']
with open('IData/Users/pipelinerun/jobs/_jobtemplate/machine3.osreg', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())

#File path for this machine: IData/Users/pipelinerun/servers/Test-03/[Instruction]
filenames = ['IData/Users/pipelinerun/jobs/_jobtemplate/head.txt','IData/Users/pipelinerun/jobs/_jobtemplate/sample1.txt', 'IData/Users/pipelinerun/jobs/_jobtemplate/template.osreg']
with open('IData/Users/pipelinerun/jobs/_jobtemplate/machine4.osreg', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())
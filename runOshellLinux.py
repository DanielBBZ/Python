from subprocess import call
from sys import argv

try:
	oscript = argv[1]
	run = argv[2]
	
	#set envirenment for Linux:
	mode="runscript"
	#mode="api"
	#oshellPath="/scratch/App/Oshell/oshell.exe"; #my oshell
	oshellPath="/IData/Users/Daniel/Leon_Oshell/oshell.exe"; #leon's oshll for 10XOptimization
	#oshellPath="/IData/Users/Daniel/App/Oshell/oshell.exe";
	#oshellPath="/IData/Users/JohnHu/oshellJH/08112017/Debug/oshell.exe"; #John's oshell
	#oshellPath="/IData/Users/Jilong/2017.04.18_Sanofi_GSA_John/ToDaniel20170613/OShellnew2/oshell.exe";
	baseFolder="/scratch/ArrayServerFile/6065/";
	tempFolder="/scratch/temp/6065/";
	monoPath="/scratch/App/mono-2.10.9/bin/mono";
	command = monoPath + " " + oshellPath + " " + "--" + mode + " " + baseFolder + " " + oscript + " " + tempFolder + " " + ">" + oscript[0:-8] +'_run' + run + '.log' + " &";
	
	#command_log = 'tail ' + '-f ' + oscript[0:-8] +'_run' + run + '.log'
	
	call (command, shell=True)
	print ('This oscript was run:' + '\n' + command)
	#print (command_log)
	#call (command_log, shell=True)

except IndexError:
	print ('Error: oscript and run counts (1 or 2 or 3 ) are excepted after the python script')
	print ('Example: python test.py test1.oscript 1')

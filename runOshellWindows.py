from subprocess import call
from sys import argv

try:
	oscript = argv[1]
	run = argv[2]
	
	#set envirenment for Linux:
	mode="runscript"
	#mode="api"
	#oshellPath="/scratch/App/Oshell/6-13-2017/oshell.exe";
	oshellPath='Z:\\Users\\Daniel\\App\\Oshell\\osheel.exe';
	#oshellPath="/IData/Users/Jilong/2017.04.18_Sanofi_GSA_John/ToDaniel20170613/OShellnew2/oshell.exe";
	baseFolder = "Z:\\Users\\Daniel\\App\\Omicsoft";
	tempFolder = "Z:\\Users\\Daniel\\App\\Temp";
	#monoPath="/scratch/App/mono-2.10.9/bin/mono";
	command = oshellPath + " " + "--" + mode + " " + baseFolder + " " + oscript + " " + tempFolder + " " + ">" + oscript[0:-8] +'_run' + run + '.log' + " &";
	
	#command_log = 'tail ' + '-f ' + oscript[0:-8] +'_run' + run + '.log'
	
	call (command, shell=True)
	print ('This oscript was run:' + '\n' + command)
	#print (command_log)
	#call (command_log, shell=True)

except IndexError:
	print ('Error: oscript and run counts (1, 2, 3 ...) are excepted after the python script')
	print ('Example: python test.py test1.oscript 1')
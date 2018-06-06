#import os
#os.path.isfile('/IData/Users/pipelinerun/jobs/_jobtemplate/scan')
import glob   
path = 'IData/Users/pipelinerun/jobs/_jobtemplate/scan/TestFileList.txt'   
regfile=glob.glob(path)
try: 
	hand =open(regfile) 
except: 
	print 'Unable to find or open file' 
	exit()
	
hand.close()
print 'registration file found'
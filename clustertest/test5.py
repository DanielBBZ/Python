lines1=[]
lines2=[]
f1=open('/Daniel/1.part')
firstfile=open('Daniel/2.part','r')
count=0
#for line in firstfile:
#	line=line.rstrip()
#	count=count+1
lines1=firstfile.readlines()
line1=lines1[0]
line2=lines1[1]

def createFile():
	file = ('/Daniel/1.part', "w+")
	file.write("%s\n%s" % (line1, line2))
	file.close()
	
	return

i=2
while i<5:
	lines2.append(lines1[i])
	i=i+1


lines3=f1.readlines()

print 'head\n',lines3

firstfile.close()
f1.close()

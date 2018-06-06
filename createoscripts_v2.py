"""
Created on Tue Aug  8 16:44:45 2017
@author: Daniel

Input files: 
    1. list.txt: contains the project names: project1.osprj \n project2.osprj
    2. script.txt: contains the oscript that 
"""


wholelist=[]

with open("list.txt") as file:
    for line in file:
        line = line.strip() #preprocess line
        line = line[:-6] #remove the ".osprj' from line if it exist
        #print (line)
        f = open("script.txt")
        contents = f.read()
        replace_contents=contents.replace("@ProjectName@", line)
        f.close()
        #print (contents)
        wholelist.append(replace_contents)

#print(wholelist)

w=open("exportQC.oscript", "w")

for element in wholelist:
    script="".join(element)
    w.write(script + "\n" + "\n")

w.close()
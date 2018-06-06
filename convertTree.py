import pandas as pd

tree = pd.read_csv('tree.txt',sep='\t',header=(0))

#get the length of the dataframe
l=tree.shape[0]

for i in range(l):
	all = tree.iat[i,0].split(".")
	new_value = ""
	for item in all:
		value = int(item)
		if value < 10:
			item = str('0')+str(value)
		new_value = new_value + "." + item
	tree.iat[i,0] = str("HP") + new_value[1:]
		
tree.to_csv("newTree.txt", header=True, index = False, sep='\t', mode='a')
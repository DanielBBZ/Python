import pandas as pd

transcript = pd.read_csv('GSM2194322.txt',sep='\t',header=(0))

#get the length of the dataframe
l=transcript.shape[0]

new_dict = {}

for i in range(l):
	all = transcript.iat[i,1]
	new_dict=dict(item.split(":") for item in all.split(";"))
	for key in new_dict:
		if new_dict[key] == "0,0":
			new_dict[key] = "0"
		elif ',' in new_dict[key]:
				new_dict[key] = new_dict[key].split(',',1)[0]
		new_dict[key] = float(new_dict[key])
	transcript.iat[i,1] = sum(new_dict.values())
	
transcript.to_csv("gene.txt", header=True, index = False, sep='\t', mode='a')
import pandas as pd

def mytranspose(filename):
	data = pd.read_csv(filename, sep='\t',header=(0))
	cols=['GeneID','CellBarcode','TranscriptNumber']
	data2=data[cols]
	Final_DF=data2.pivot(index='GeneID', columns='CellBarcode', values='TranscriptNumber').fillna('0')
	name=filename.replace(' ', '')[:-4] + "_"
	Final_DF.columns = name + Final_DF.columns
	return Final_DF

# d1 = mytranspose('table.txt')
# d2 = mytranspose('table2.txt')
# result = pd.merge(Merged_DF, table, how='outer', left_index=True, right_index=True)
# result.fillna('0', inplace=True)

# print (result)
Merged_DF = pd.DataFrame()

with open("list.txt") as file:
	for line in file:
		line = line.strip() #preprocess line
		table=mytranspose(line)
		Merged_DF=pd.merge(Merged_DF, table, how='outer', left_index=True, right_index=True)
		Merged_DF.fillna('0', inplace=True)


Merged_DF.to_csv("merged.txt", header=True, index = True, sep='\t', mode='a')
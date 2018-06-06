# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 10:40:51 2017

@author: Daniel
"""

import pandas as pd

barcodefile = pd.read_csv('barcode.txt',sep='\t',header=(0))
samplefile = pd.read_csv('sample.txt',sep='\t',header=(0))

new_dict = {}
#create a dictionary based on the separate maps
for i in range(32):
	for j in range(96):
		value = samplefile.iat[i,0] + "_" + barcodefile.iat[j,0]
		key = samplefile.iat[i,1] + "_" + str(barcodefile.iat[j,1])
		new_dict[key] = value

len (new_dict)

df = pd.read_csv('cell_type_annotation_Cels2016_new.csv',sep='\t',header=(0))

df1 = df.transpose()

#Set the column labels to equal the values in the 1st row (index location 0):
df1.columns = df1.iloc[0]

#Drop the 1st row
#df.reindex(df.index.drop(0))
#keep the 1st row here as we would like to have this information

#create Serie from columns of count by to_series which are map by dictionary:
df1.columns = df1.columns.to_series().map(new_dict)

df2 = df1.transpose()

df2.columns = ['DonorID', 'CellType']
df2.index.rename('SampleID', inplace=True)

df2.to_csv("CellType.txt",header=True, index = True, sep='\t', mode='a')
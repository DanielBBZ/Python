# purpose: transform the value in the count table to be therotical value
# and map the Ensemble gene ID to gene Name as row index
# and rename the column name to remove the middle strings




import pandas as pd
import numpy as np

#read text file with first column as index column
df = pd.read_csv('SingleCellCounts.txt',sep='\t',header=(0), index_col=(0))

gene = pd.read_csv('Annotation.txt', sep='\t', header=(0))

total = 256.0

def TConvert(m):
    if m ==256:
        m-=1
    new_m = round(abs(total * np.log(1 - m/total)),2)
    return new_m


df_new = df.applymap(TConvert)

gene_dict = {}

gene_num = gene.shape[0]

for i in range(gene_num):
    gene_dict[gene.iat[i,0]] = gene.iat[i,1]

df_new.index = df_new.index.to_series().map(gene_dict)


#rename the column name, removing the middle strings
df_new = df_new.rename(columns = {col: col.split('_')[0] + '_' + col.split('_')[2].split('.')[2] for col in df_new.columns})

#check with first 5 rows to see
#df_new.head(n=5)

#df.to_csv('count_table.txt', sep='\t', index=True)
df_new.to_csv('TCount.txt', header=True, index = True, sep='\t', mode='a')

import pandas as pd

count = pd.read_csv('Count.txt',sep='\t',header=(0))

def RPM(df):
	result = df.copy()
	for feature_name in df.columns:
		if 'SRX' not in feature_name:
			continue
		else:
			value = 1000000/df[feature_name].sum()
			result[feature_name] = df[feature_name] * value
	return result

#drop the last column as the last column is mean:
new_data=RPM(count)
new_data.drop(new_data.columns[len(new_data.columns)-1], axis=1, inplace=True)

new_data.to_csv("Normalized.txt", header=True, index = True, sep='\t', mode='a')
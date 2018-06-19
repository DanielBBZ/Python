filenames = ['/workspace/ws03/IData/Users/Daniel/Support/clustertest/folder1/text1.txt','/workspace/ws03/IData/Users/Daniel/Support/clustertest/folder1/text2.txt', '/workspace/ws03/IData/Users/Daniel/Support/clustertest/folder1/text3.txt']
with open('/workspace/ws03/IData/Users/Daniel/Support/clustertest/folder2/text.txt', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())
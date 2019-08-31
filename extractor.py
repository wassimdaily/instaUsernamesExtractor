
def extarct():

	import main, re
	opFile = open('txt/in.txt', "r").read()
	writer = open('txt/usernames.txt', "w")
	searcher = re.findall(r'\busername\b.:..............', opFile)
	writer.write(str(searcher))
	print('result: '+str(searcher))
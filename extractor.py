def extarct():
	import main, re
	expr = r'\busername\b.:..............'
	opFile = open('txt/in.txt', "r").read()
	searcher = re.findall(expr, opFile)
	print(searcher)
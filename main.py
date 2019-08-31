# main file 
import requests as tool
from bs4 import BeautifulSoup
import userAgent as agent , postInput
import extractor
with tool.Session() as s:

	res = s.get(postInput.post, headers=agent.userAgent)		
	par = BeautifulSoup(res.content, 'html.parser')
	writeOn = open('txt/in.txt', "w")
	writeOn.write(str(par))
	extractor.extarct()

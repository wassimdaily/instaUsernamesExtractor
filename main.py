# test class using for test the project 
import requests as tool
from bs4 import BeautifulSoup
import json
import re
import userAgent as agent , postInput

with tool.Session() as s:

	res = s.get(postInput.post, headers=agent.userAgent)		
	par = BeautifulSoup(res.content, 'html.parser')
	print(par)
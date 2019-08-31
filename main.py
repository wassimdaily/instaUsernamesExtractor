# test class using for test the project 
import requests as tool
from bs4 import BeautifulSoup
import json
import re
post = 'https://www.instagram.com/p/B1msxg9HVny/'

userAgent = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


with tool.Session() as s:

	res = s.get(post, headers=userAgent)		
	par = BeautifulSoup(res.content, 'html.parser')
	
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from lxml import html
import requests

linenum = 1
with open('links.txt','r') as f, \
	 open('export.txt','w') as export:
	lines = f.readlines()
	for line in lines:
		req = Request(line, headers={'User-Agent': 'Mozilla/5.0'})
		html_page = urlopen(req)
		soup = BeautifulSoup(html_page, "lxml")

		category = soup.find('ul', class_="clearfix mod-crumb")
		iferror = soup.find_all('div', class_="info warning clearfix site-notice")

		if len(iferror) > 0:
			print("Mod #" + str(linenum) + " is unavailable")
			continue

		ex = str(category.contents[7].contents[1].string)
		print(ex.replace("\n",""))
		export.write(ex)
		linenum += 1
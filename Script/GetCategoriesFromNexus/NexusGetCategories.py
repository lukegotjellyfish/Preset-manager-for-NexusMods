from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from lxml import html
import requests
import time
import re

dictList  = []

def add_another(input_url, filename):
    req = Request(input_url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    replacement = ["<ul class=\"choice-list\">\n",
    "\n<input id=\"has_images\" name=\"has_images\" type=\"checkbox\" value=\"1\"/>",
    "\n<label for=\"has_images\">",
    "\n<span class=\"choice-check\"></span>",
    "\n<span class=\"check-label\">NMM compatible</span>",
    "\n</label>",
    "\n</li>",
    "\n<li>",
    "\n<input disabled=\"disabled\" id=\"include_adult\" name=\"include_adult\" type=\"checkbox\" value=\"1\"/>",
    "\n<label for=\"include_adult\">",
    "\n<span class=\"check-label\">Include adult files</span>",
    "\n<input disabled=\"disabled\" id=\"only_adult\" name=\"only_adult\" type=\"checkbox\" value=\"1\"/>",
    "\n<label for=\"only_adult\">",
    "\n<span class=\"check-label\">Only show adult files</span>",
    "<li>\n",
    "\n</ul>"]
    alls = soup.find_all("ul", {"class": "choice-list"})
    temp = str(alls[0])
    for x in replacement:
        temp = temp.replace(x,"")
    temp = re.sub("<span class=\"check-category\">.*</span>\n", "", temp)
    temp = re.sub("<input id=\"cat.*\" name=\"categories\[\]\" type=\"checkbox\" value=\".*\"/>\n", "", temp)
    temp = re.sub("<label for=\"cat(.*)\">\n<span class=\"check-label\">(.*)</span>", "	\"\g<1>\": \"\g<2>\",", temp)
    #temp = re.sub("\n", "", temp)
    temp = filename + " = {\n" + temp[:-1] + "\n}\n"
    print(temp)
    dictList.append(temp)



##START##
with open("links.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        title = line.replace("https://www.nexusmods.com/","").replace("/mods","").replace("\n","")
        add_another(line, title)
        time.sleep(2)

with open("dictionaries.txt", "w") as f:
    for item in dictList:
        f.write(item)
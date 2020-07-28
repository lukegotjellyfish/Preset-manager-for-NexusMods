import requests
import time
import re
import ast
import random
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from lxml import html


#Function repurposed from SteamCollectionSizeFinder
def add_another(input_url, gamename):
    #Request URL with Firefox identity
    req = Request(input_url, headers={'User-Agent': 'Mozilla/5.0'})
    #Open page to var
    html_page = urlopen(req)
    #Init BS4 with page as lxml
    soup = BeautifulSoup(html_page, "lxml")

    #Text replacement list
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
    #Get all choice-lists (categories and attributes)
    alls = soup.find_all("ul", {"class": "choice-list"})
    #First list is categories
    temp = str(alls[0])
    #Iterate through replacement strings to remove them from temp
    for x in replacement:
        temp = temp.replace(x,"")
    #Use regex rules to further strip category list into a usable format
    temp = re.sub("<span class=\"check-category\">.*</span>\n", "", temp)
    temp = re.sub("<span class=\"check-category\">.*</span>", "", temp)
    temp = re.sub("<input id=\"cat.*\" name=\"categories\[\]\" type=\"checkbox\" value=\".*\"/>\n", "", temp)
    temp = re.sub("<label for=\"cat(.*)\">\n<span class=\"check-label\">(.*)</span>", "\"\g<1>\": \"\g<2>\",", temp)

    #Create evalTemp as a string dictionary
    evalTemp = "{" + temp[:-1] + "}"
    #Eval evalTempt as a dictionary using ast
    tempDict = ast.literal_eval(evalTemp)
    #Sort dictionary by key values
    tempDict = sorted(tempDict.items())
    #Convert dictionary into string to format and save
    stringDict = str(tempDict)

    #Remove dictionary items from (x:y),(z:c) format
    stringDict = re.sub("\('([^\)]*)', '([^\)]*)'\)", "\n		\"\g<1>\": \"\g<2>\"", stringDict)
    #Strip leading and ending [], replace with python dictionary format
    stringDict = stringDict.replace("[", "	" + gamename + " = {").replace("]","\n	}\n")
    #Print dictionary to preview
    print(stringDict)
   
    with open(filename, "a") as f:
        f.write(stringDict)

##START##
filename = "dictionaries.txt"
if os.path.isfile("./dictionaries.txt"):
    x = 1
    while os.path.isfile("./dictionaries" + str(x) + ".txt") is True:
        x += 1
    filename = "dictionaries" + str(x) + ".txt"
with open(filename, "w") as f:
    f.write("nexus_dictionaries = {\n")

with open("links.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        title = line.replace("https://www.nexusmods.com/","").replace("/mods","").replace("\n","")
        add_another(line, title)
        #1 second delay to be kind to nexus's servers
        time.sleep(1)

#end dict
with open(filename, "a") as f:
    f.write("\n}")
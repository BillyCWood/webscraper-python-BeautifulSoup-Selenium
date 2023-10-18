from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


#modify attr in tag
#tag = doc.find("option")
#tag['selected'] = False
#add an attr
#tag['color'] = "blue"


#find a list of tags
tags = doc.find_all(['p', 'div', 'li'])
print(tags)

#search for a combination of queries; can search for specific values of tags
tags = doc.find_all(["option"], text="Undergraduate", value="undergraduate")
print(tags)



#-----------------------------
#find class names

tags = doc.find_all(class_="btn-item")
print(tags)



#-----------------------------
#search with regex
tags = doc.find_all(string=re.compile("\$.*"))
for tag in tags:
    print(tag.strip())


#-----------------------------
#Limit number of results in search
tags = doc.find_all(string=re.compile("\$.*"), limit=1)
for tag in tags:
    print(tag.strip())



#-----------------------------
#Save modified HTML
tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc))
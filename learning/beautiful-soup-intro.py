#reading html files
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    #BS(doc to read, specify the parser for the document)
    doc = BeautifulSoup(f, "html.parser")

#print(doc)

#finding tags
tag = doc.title

#modify tag in place
#tag.string = "hello"
#print(tag.string)

#only returns the first occurence
tag = doc.find("a")

# get all occurences of the specified tag
#can be indexed
tags = doc.find_all("p")

#get the all of the b tags contained with in the first occurence of the p tags
#tags = doc.find_all("p")[0]
#print(tags.find_all("b"))


print(tags)


from bs4 import BeautifulSoup
import requests

url = "https://www.thriftbooks.com/w/knowing-god_ji-packer/245803/#edition=1842375&idiq=3816643"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

#find text within the doc in addition to tags

#this will only return the $. No numbers afterwards.
prices = doc.find_all(string="$")
#print(prices)

#We need to access the parent in order to get the whole price
parent = prices[1].parent
print(parent)
#strong = parent.find("strong")
#print(strong.string)

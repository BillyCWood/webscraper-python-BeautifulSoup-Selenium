from bs4 import BeautifulSoup
import requests
import re


url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")



#-----------------------------
#looking for tbody tag
tbody = doc.tbody
#print(tbody)


#-----------------------------
#elements that are on the same level in the tree
trs = tbody.contents
#print(trs[0].next_sibling)
#print(trs[1].previous_sibling)
#print(list(trs[0].next_siblings))


#-----------------------------
#get partent
#print(trs[0].parent)
#print(trs[0].parent.name)


#-----------------------------
#get descendents/content
#print(list(trs[0].descendants))


#-----------------------------
#Getting crypto prices
prices = {}

for tr in trs[:10]:
    #td = table data
    name, price =  tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

for tr in trs[10:]:
    name, price = tr.contents[2:4]
    fixed_name = name.find("span", string=re.compile("[A-Z]+")).string
    fixed_price = price.text
    prices[fixed_name] = fixed_price

k = 1


print()
print("NAME".rjust(9), "PRICE".rjust(22))
print("----".rjust(9), "-----".rjust(22))
for key in prices:
    print((str(k) + ".").ljust(4), str(key).ljust(21), prices[key])
    k+=1

print()



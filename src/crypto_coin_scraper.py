from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import schedule
import time


# Author: Billy Wood
#
#
#
# Web scraper to automtically and continuously request data from crypto currency website
# and display in real time the changes of the market,
# being displayed within a GUI




def webscraper():
    
    driver = webdriver.Chrome()
    driver.get("https://coinmarketcap.com/")
    # Sleeping to make sure that we actually get updated values
    # each call rather than get the same exact prices
    # as the initial call infinitely
    time.sleep(4)

    doc = BeautifulSoup(driver.page_source, 'html.parser')




    tbody = doc.tbody
    trs = tbody.contents
     
    cryptocurrencies = {}

    coin_names = []

    # Must specify finding from tbody or else we well get entries
    # from divs preceding the tbody
    names = tbody.find_all('p', {'class' : 'sc-4984dd93-0 kKpPOn'})
    cis = tbody.find_all('p', {'class' : 'sc-4984dd93-0 iqdbQL coin-item-symbol'})

    for i in range(len(names)):

        # Get name and abbreviation stored together
        coin_names.append(names[i].text)
        coin_names[i] = coin_names[i] + " - " + cis[i].text

        # Get price
        price = trs[i].contents[3]
        fixed_price = price.text

        # Store information in dictionary
        cryptocurrencies[coin_names[i]] = fixed_price
    
    
    # Store values physically
    write_crypto_data(cryptocurrencies)


    # Display crypto information stored in dictionary
    k = 1
    print()
    print("NAME".rjust(9), "PRICE".rjust(26))
    print("----".rjust(9), "-----".rjust(26))
    for key in cryptocurrencies:
        print((str(k) + ".").ljust(4), str(key).ljust(25), cryptocurrencies[key])
        k+=1

    print()
    
    driver.quit()


# Create csv file to physically store the data being scraped for visualization
def write_crypto_data(dictionary: dict):
    with open("crypto.csv", 'a+', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=dictionary.keys())
        
        # Seeking to the beginning of the file so that our
        # read if-statement functions properly
        csvfile.seek(0)
        if len(csvfile.read()) < 1:
            writer.writeheader()
        
            # Remove commas and dollar signs from dictionary values
            # and convert to float for the purpose of data viz with
            # numerical values
            writer.writerow({k : float(v.replace(',', '').replace('$', '')) for k, v in dictionary.items()})
        

        else:
            # Make sure that we are appending to the end of the file
            # after previously seeking to the beginning of the file
            csvfile.seek(2)
            writer.writerow({k : float(v.replace(',', '').replace('$', '')) for k, v in dictionary.items()})
        

# initial call
webscraper()


# automation
schedule.every(10).seconds.do(webscraper)

while True:
    schedule.run_pending()
    time.sleep(1)

#This file gets takes URL and desired price, and gets product name and price from js file

import sys
import csv

import web_scraper

print("Python file: new_site.py entered...")
print("new_site.py attempting to read URL and desiredPrice....")


#sys.argv[1] & [2] piped in from index.js file and we are grabbing them here.
URL = str(sys.argv[1])
desiredPrice = int(sys.argv[2])

print("Python file new_site.py reading URL: " + URL)
print("Python file new_site.py Recieved desired user price at: " + str(desiredPrice))


#TODO: validate URL is a valid one that returns an int value when web scraped. 

websiteName = "Amazon"

print("new_site.py attempting to read Product Name...")

productName = web_scraper.getProductName(URL)

print("new_site.py saved productName as: " + productName)



print("new_site.py attempting to read Product Price...")

productPrice = web_scraper.getProductPrice(URL)

print("new_site.py saved product price as: " + str(productPrice))

#Checking that desiredPrice is lower than productPrice otherwise every check would flag a positive
if desiredPrice >= productPrice:
    raise ValueError("The Price is already lower than or equal to what you are looking for!")


data = [websiteName, productName, productPrice, desiredPrice, URL]

#Saves the given values to an external text file
print("periodic_checker attempting to save values to file...")
with open('saved_data.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    print("sucessfully saved to file")

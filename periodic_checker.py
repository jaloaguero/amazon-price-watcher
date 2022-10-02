#opens csv file then iterates through it comparing the user desired price to the newest web scraped price

import csv
import web_scraper

print("Performing periodic check...")


f = csv.reader(open('saved_data.csv',"r"), delimiter=",")
#row[0] is the website (tbh dont need this just marking it in case in the future this expands)
#row[1] is the name of the product
#row[2] is the last recorded price
#row[3] is the desiredPrice
#row[4] is the URL
#newPrice is the newest price
for row in f:
    print(row[4])
    print("Name: " + row[1] + " Desired Price: " + row[3] + "...")
    newPrice = web_scraper.getProductPrice(row[4])
    print("Updated Price: " + str(newPrice))
    if newPrice <= float(row[3]):
        #TODO: Make sure this exports upwards somehow idk how yet but look into it otherwise this does nothing
        print("SALE!!!!! on " + row[1])
        #maybe we need to print this all out lol
        #print(row)

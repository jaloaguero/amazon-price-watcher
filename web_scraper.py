import requests
from bs4 import BeautifulSoup

#data to give to website to essentially make it think we are not a bot (even tho we are >:( )
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

#TODO: first 2 lines of these functions are the same, figure out a way to not have this code repeat
#I don't want to call requests twice for the exact same info, would rather call once and simply use it.
def getProductPrice(URL):
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("span", class_="a-offscreen")
    results = results.text.strip().replace('$','').replace(',','')
    return float(results)

def getProductName(URL):
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup)
    #old class: a-size-large product-title-word-break
    results = soup.find("span", attrs={"id": 'productTitle'})
    results = results.text.strip()
    return results

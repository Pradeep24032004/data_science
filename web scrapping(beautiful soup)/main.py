import pandas as pd
import requests
from bs4 import BeautifulSoup
#for i in range(2,10):
Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(1, 7):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)


    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="DOjaWF gdgoEp")
    names = box.find_all("div", class_="KzDlHZ")

    for i in names:
        name = i.text
        Product_name.append(name)
    #print(Product_name)

    prices = box.find_all("div", class_="hl05eU")

    for i in prices:
        name = i.text
        Prices.append(name)

    #print(Prices)

    desc = box.find_all("ul", class_="G4BRas")

    for i in desc:
        name = i.text
        Description.append(name)

    #print(Description)

    reviews = box.find_all("div", class_="XQDdHH")

    for i in reviews:
        name = i.text
        Reviews.append(name)

    #print(Reviews)

df = pd.DataFrame({"Product Name":Product_name, "Prices":Prices, "Description":Description, "Reviews":Reviews})

df.to_csv("Flipkart_mobiles_under_50000.csv")
#print(df)

























    #while True:
    # nextpage - np, next page element in flipkart website
    #np = soup.find("a", class_="_9QVEpD").get("href")
    #cnp = "https://www.flipkart.com" + np
    #print(cnp)
    # print(soup)

    #url = cnp
    #r = requests.get(url)
    #soup = BeautifulSoup(r.text, "lxml")




import requests
from bs4 import BeautifulSoup
import pandas

search_item=input("item:")

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
req=requests.get("https://www.flipkart.com/search?q={}".format(search_item),headers=headers)

products=[]
prices=[]
ratings=[]
properties=[]
content=req.content
soup=BeautifulSoup(content,"html.parser")
for a in soup.findAll("a",href=True,attrs={"class":"_31qSD5"}):
	product=a.find("div",attrs={"class":"_3wU53n"})
	price=a.find("div",attrs={"class":"_6BWGkk"})
	propertie=a.find("div",attrs={"class":"_3ULzGw"})
	rating=a.find("div",attrs={"class":"niH0FQ"})
	products.append(product.text)
	prices.append(price.text)
	properties.append(propertie.text)
	ratings.append(rating.text)

df = pandas.DataFrame(
{"Product Name":products,"ProductDestails":properties,"Price":prices,"Rating":ratings})
df.to_csv("flipkart({}).csv".format(search_item),index=False)

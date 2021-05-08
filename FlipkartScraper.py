from urllib.request import Request, urlopen
import requests
import bs4
from bs4 import BeautifulSoup
import json
from flask_restful import Resource
import time
import json

class FlipkartScrape(Resource):
    def flipkartScrape(self,keyword):
        query=keyword.split(" ")
        query='%20'.join(query)
        urlflipkart="https://www.flipkart.com/search?q="+query+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        print(urlflipkart)
        rq=Request(urlflipkart,headers={'User-Agent': 'Mozilla/5.0'})
        src=urlopen(rq)
        html = src.read()
        soup=BeautifulSoup(html,'html.parser')
        Elements=soup.findAll('div',{"class":"_1AtVbE col-12-12"})
        eDict={}
        i=0
        for Element in Elements:
            try:
                elemcontainer=Element.find('a',{'class':'_1fQZEK'})
                title=elemcontainer.find('div',{'class':'_4rR01T'}).text
                imgurl=elemcontainer.find('img')['src']
                pricetxt=elemcontainer.find('div',{'class':'_30jeq3 _1_WHN1'}).text
                price=pricetxt[1:]
                price=int(price.replace(',',''))
                tmp={'title':title,
                'price':price,
                'imageURL':imgurl}
                eDict[str(i)]=tmp
                i+=1
            except:
                continue
        return json.dumps(eDict)

    def get(self,keyword):
        myobj=json.loads(self.flipkartScrape(keyword))
        return myobj

if __name__=='__main__':
    obj= FlipkartScrape()
    print(obj.flipkartScrape('iphone 11'))
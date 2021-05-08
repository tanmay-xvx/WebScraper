from urllib.request import urlopen
import requests
import bs4
from bs4 import BeautifulSoup
import json
from flask_restful import Resource
import time
import json

class AmazonScrape(Resource):
    
    def amazonScrape(self,keyword):
        query=keyword.split(" ")
        query="+".join(query)
        urlamazon="https://www.amazon.in/s?k="+query+"&ref=nb_sb_noss"
        print(urlamazon)
        # rq=Request(urlamazon,headers={'User-Agent': 'Mozilla/5.0'})
        src=urlopen(urlamazon)
        # src=requests.get(urlamazon)
        html = src.read()
        soup=BeautifulSoup(html,'html.parser')
        Elements=soup.findAll('div',{"class":"s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16"})
        eDict={}
        i=0
        for Element in Elements:
            try:
                elemcontainer=Element.find('div',{'class':'sg-row'}).findNext('div',{'class':'sg-row'})
                title=elemcontainer.find('h2').text.replace('\n','')
                imgurl=elemcontainer.find('img')['src']
                pricetxt=elemcontainer.find('span',{'class':'a-offscreen'}).text
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
        myobj=json.loads(self.amazonScrape(keyword))
        return myobj

if __name__=='__main__':
    obj= AmazonScrape()
    print(obj.amazonScrape('iphone 11'))
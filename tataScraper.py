from urllib.request import Request, urlopen
import requests
import bs4
from bs4 import BeautifulSoup
import json
from flask_restful import Resource
import time
import json

class TataScrape(Resource):
    def tataCliqScrape(self,keyword):
        query=keyword.split(" ")
        query='%20'.join(query)
        urlCliq="https://www.tatacliq.com/search/?searchCategory=all&text="+query
        print(urlCliq)
        # rq=Request(urlCliq,headers={'User-Agent': 'Mozilla/5.0'})
        # src=urlopen(rq)
        src=requests.get(urlCliq)
        html = src.text
        soup=BeautifulSoup(html,'html.parser')
        Elements=soup.findAll('div',{"class":"Grid__element"})
        eDict={}
        i=0
        for Element in Elements:
            try:
                elemcontainer=Element.find('div',{'class':'ProductModule__base'})
                title=elemcontainer.find('div',{'class':'ProductDescription__content'}).find('h2').text
                imgurl=elemcontainer.find('img')['src']
                pricetxt=elemcontainer.find('div',{'class':'ProductDescription__content'}).find('h3').text
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
        myobj=self.tataCliqScrape(keyword)
        return myobj

if __name__=='__main__':
    obj= TataScrape()
    print(obj.tataCliqScrape('iphone 11'))
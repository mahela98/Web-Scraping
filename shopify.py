import requests
import json
# import dataset


class ShopifyScraper():
    def __init__(self,baseurl):
        self.baseurl = baseurl
        
    def downloadJson(self,pageNumber):
        r= requests.get(self.baseurl + f'products.json?limit=250&page={pageNumber}',timeout=20)
        if r.status_code !=200:
            print('Error : ' , r.status_code)
        
        if len(r.json()['products']) > 0:
            data = r.json()['products']
            return data

        else:
            return


    def parsejson(self,jsondata):
        print(jsondata)



all = ShopifyScraper('https://www.allbirds.co.uk/')
data = all.downloadJson(1)

print(data)
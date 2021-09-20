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
        products=[]
        for product in jsondata:
            print(len(jsondata))
            mainId= product['id']
            mainTitle=product['title']
            vendor= product['vendor']
            product_type= product['product_type']
            for variant in product['variants']:
                item={
                    'id':mainId,
                    'product_type':product_type,
                    'mainTitle':mainTitle,
                    'vendor':vendor,
                    'variantId': variant['id'],
                    'vTitle': variant['title'],
                    'requires_shipping': variant['requires_shipping'],
                    'taxable': variant['taxable'],
                    'available': variant['available'],
                    'created_at': variant['created_at'],
                    'updated_at': variant['updated_at'],
                    'price': variant['price'],
                    'position': variant['position'],
                }
                products.append(item)
           
            print('product length : '+ len(products))
            return products


            

def main():
    all = ShopifyScraper('https://www.allbirds.co.uk/')
    allPagePesults=[]
    for page in range(1,10):
        data = all.downloadJson(page)
        # print(data)
        print('Getting data from: ',page)
        try:
            allPagePesults.append(all.parsejson(data))
            # print(all.parsejson(data))
        except:
            print(f'completed , pages = {page -1}')
            break
    return allPagePesults


products=main()
# print(products)

totalProducts = [item for i in products for item in i]

print(len(totalProducts))






# print(data)
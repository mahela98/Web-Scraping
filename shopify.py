import requests
import json
# import dataset4


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
        productsArray=[]
        for product in jsondata:
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
                productsArray.append(item)  
        return productsArray


            

def main():
    all = ShopifyScraper('https://www.allbirds.co.uk/')
    allPagePesults=[]
    for page in range(1,10):
        data = all.downloadJson(page)
        print('Getting data from: ',page)
        try:
            allPagePesults.append(all.parsejson(data))
        except:
            print(f'completed , pages = {page -1}')
            break
    return allPagePesults


products=main()
totalProducts = [item for i in products for item in i]
print('Total Products',len(totalProducts))

# if __name__ == '__main__':

#     # db = dataset.connect('location')
#     # table = db.create_table('products',primary_id='variantId')
#     # products=main()
#     # totalProducts = [item for i in products for item in i]
#     print('Total Products',len(totalProducts))

#     # for p in totalProducts:
#     #     if not table.find_one(variantId=p['variantId']):
#     #         table.insert(p) 
#     #         print('new product :' , p)






# print(data)
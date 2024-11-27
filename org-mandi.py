import requests
import bs4

def fetch_product_data(url):
    
    response = requests.get(url)
    
    
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    
    
    price = soup.find_all(class_="displayed-price")
    name = soup.find_all(class_="product-card-title h6 text-left")
    quantity= soup.find_all(class_="variant-selector")
    
   
    for i in range(len(name)):
         print(name[i].text.strip(),end= '  --  ') 
        
         print(price[i].text,end='  --  ')
        
         print(quantity[i].text)
        
       
        
print('PRODUCT-NAME','--','PRICE','--','Quantity')        
print('----------------------------------------------------------------')

url = 'https://organicmandya.com/collections/personal-care-1'
print('<---PERSONAL-CARE---->')
fetch_product_data(url)
print('')

print('<---STAPLES--->')
fetch_product_data('https://organicmandya.com/collections/staples')
print('')

print('<---SNACKS-->')
fetch_product_data('https://organicmandya.com/collections/snacks')
print('')  

print('<---"OILS"-->')
fetch_product_data('https://organicmandya.com/collections/edible-oils')
print('')

print('<---"RTC"-->')
fetch_product_data('https://organicmandya.com/collections/ready-to-cook')
print('')

print('<---"Beverages"-->')
fetch_product_data('https://organicmandya.com/collections/beverages')
print('')

print('<---"DAIRY-PRODUCTS"-->')
fetch_product_data('https://organicmandya.com/collections/a2-dairy-products')
print('')

print('<---"FRUITS-VEG"-->')
fetch_product_data('https://organicmandya.com/collections/fruits-vegetables')
print('')

print('<---"HOME-ESSENTIALS"-->')
fetch_product_data('https://organicmandya.com/collections/home-essential')
print('')

print('<---"SEEDS"-->')
fetch_product_data('https://organicmandya.com/collections/dry-fruits-seeds')










    







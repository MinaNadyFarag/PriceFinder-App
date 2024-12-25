import requests
from bs4 import BeautifulSoup
from threading import Thread, Lock

results = []

lock = Lock()
def amazon_scraping (productText):
    try:
        url = f"https://www.amazon.com/s?k={productText.replace(' ', '+')}"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

        }
        response = requests.get(url, headers = header)
        soup = BeautifulSoup(response.content, "html.parser")
        product = soup.find("span", class_= "a-size-medium a-color-base a-text-normal")
        price = soup.find("span", class_= "a-price-whole")
        
        if product and price:
            product_name = product.text.strip()
            product_price = float(price.text.replace(",", "").strip())
            
            with lock:
                results.append({"Site Name": "Amazon", "Product Name": product_name, "Price": product_price})
            
    except Exception as e:
        print(f"Error:{e}, while scrapping amazon")
        
        
def scrape_ebay(product_name):
    try:
        url = f"https://www.ebay.com/sch/i.html?_nkw={product_name.replace(' ', '+')}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        product = soup.find("h3", class_="s-item__title")
        price = soup.find("span", class_="s-item__price")
        
        if product and price:
            product_name = product.text.strip()
            product_price = float(price.text.replace("$", "").replace(",", "").strip())
            
            with lock:
                results.append({"site": "eBay", "name": product_name, "price": product_price})
    except Exception as e:
        print(f"Error scraping eBay: {e}")

def scrape_walmart(product_name):
    try:
        url = f"https://www.walmart.com/search?q={product_name.replace(' ', '+')}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        product = soup.find("a", class_="product-title-link line-clamp line-clamp-2")
        price = soup.find("span", class_="price-characteristic")
        
        if product and price:
            product_name = product.text.strip()
            product_price = float(price['content'].strip())
            
            with lock:
                results.append({"site": "Walmart", "name": product_name, "price": product_price})
    except Exception as e:
        print(f"Error scraping Walmart: {e}")

def find_lowest_price():
    if not results:
        print("No results found.")
        return
    lowest = min(results, key=lambda x: x['price'])
    print("\nLowest Price Found:")
    print(f"Site: {lowest['site']}")
    print(f"Product: {lowest['name']}")
    print(f"Price: ${lowest['price']:.2f}")

if __name__ == "__main__":
    product_name = input("Enter the product name: ")
    
    # Threads for different sites
    threads = [
        Thread(target=amazon_scraping, args=(product_name,)),
        Thread(target=scrape_ebay, args=(product_name,)),
        Thread(target=scrape_walmart, args=(product_name,))
    ]
    
    # Start threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    # Display the result
    find_lowest_price()
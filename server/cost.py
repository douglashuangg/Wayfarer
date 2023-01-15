import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.option import Options 


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
start_url = 'https://www.loblaws.ca/food/fruits-vegetables/c/28000?navid=flyout-L2-fruits-vegetables'
driver.get(start_url)
import time
time.sleep(20)
page_source = driver.page_source
print('product-name__item product-name__item--name' in page_source)

for (all items existing) in zip(mutliple list)

url = "http://www.example.com/attraction"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

cost = soup.find("span", class_="attraction-cost").text
print(cost)
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# url = "http://www.example.com/attraction"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# cost = soup.find("span", class_="attraction-cost").text
# print(cost)

def getOperatingHours(attraction, date):
  days = date.split(" ")
  text = attraction+"hours"+days[0]
  engineeredPrompt = text.replace(" ", "+")
  url = 'https://www.google.com/search?q=cn+tower+hours+july+2&rlz=1C1CHBF_enCA967CA967&oq=cn+tower+hours+july+2&aqs=chrome..69i57j33i10i160l3j33i22i29i30.2791j0j7&sourceid=chrome&ie=UTF-8'

  driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
  url = "http://www.google.com/search?q=" + engineeredPrompt
  driver.get(url)
  soup = BeautifulSoup(driver.page_source, 'html.parser')

  search = soup.find_all('span', class_="TLou0b JjSWRd")
  operatingHours = search[0].getText()
  driver.close()

  return operatingHours

getOperatingHours()
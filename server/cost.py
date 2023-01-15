import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



# url = "http://www.example.com/attraction"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# cost = soup.find("span", class_="attraction-cost").text
# print(cost)

def getOperatingHours():
  text = "ROM Hours July 2"
  engineeredPrompt = text.replace(" ", "+")
  url = 'https://google.com/search?q=' + engineeredPrompt
 # TLou0b JjSWRd
  driver = webdriver.Chrome()
 
  driver.get(url)
  WebDriverWait(driver=driver, timeout=5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'qrShPb kno-ecr-pt PZPZlf q8U8x')))
  print(driver.page_source)
  hours = driver.find_element(By.CLASS_NAME, 'qrShPb kno-ecr-pt PZPZlf q8U8x')
#   hours = driver.find_elements_by_class_name('TLou0b JjSWRd')
  print(hours)
# 
#   search_box = driver.findElements(By.className("gLFyf"));

#   search_box.send_keys(text)
#   print(search_box)
#   search_box = driver.find_element_by_xpath("//input[@name='q']")
#   search_box.submit()
#   page_source = driver.page_source
# #   driver.get("https://www.twitch.tv/directory/game/Art")

#   request_result = requests.get(url)
# #   print(request_result.content)
#   soup = BeautifulSoup(page_source, "html.parser")
#   operatingHours = soup.find_all("span")
#   operatingHours = soup.find("span", class_='dfB0uf')
#   print(operatingHours)
#   driver.close()
  operatingHours = []

  return operatingHours

getOperatingHours()
import requests
from bs4 import BeautifulSoup
import lxml

# url = "http://www.example.com/attraction"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# cost = soup.find("span", class_="attraction-cost").text
# print(cost)

def getOperatingHours():
  text = "ROM Hours July 2"
  url = 'https://google.com/search?q=' + text
  request_result = requests.get(url)
#   print(request_result.content)
  soup = BeautifulSoup(request_result.content, "html.parser")
#   operatingHours = soup.find_all("span")
  operatingHours = soup.find("span", class_='dfB0uf')
  print(operatingHours)
  return operatingHours

getOperatingHours()
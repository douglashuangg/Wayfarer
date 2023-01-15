import requests
from bs4 import BeautifulSoup

url = "http://www.example.com/attraction"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

cost = soup.find("span", class_="attraction-cost").text
print(cost)
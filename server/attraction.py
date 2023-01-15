from serpapi import GoogleSearch
import requests
from price_generator import generate_price

GoogleSearch.SERP_API_KEY = "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9"

def getAttraction(keywords):
  # location = keywords[0];
  # need to grab the keyword array from kewords.py
  location = keywords[0]
  # keywords[0]

  params = {
    "engine": "google",
    "q": "Top sights in " + location, 
    #change toronto to location after testing
    "location": location,
    "api_key": "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9",
    "num": 15
    }

  search = GoogleSearch(params)
  results = search.get_dict()
  
  sights =  [sight.get("title") for sight in results.get("top_sights").get("sights")]
  description = [sight.get("description") for sight in results.get("top_sights").get("sights")]
  links = [sight.get("link") for sight in results.get("top_sights").get("sights")]
  images = [sight.get("thumbnail") for sight in results.get("top_sights").get("sights")]
  # operationLink = links[0]
  # api_key = "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9"
  # url = operationLink

  # query = url
  # url = f"https://serpapi.com/search?q={query}&api_key={api_key}"

  # response = requests.get(url)
  # data = response.json()
  # hours = data["hours"]

  # print(hours)
  outer = []
  destination = []
  for i in range (0,5):
    listing = {
        "name": sights[i],
        "description": description[i],
        "links": links[i],
        "images": images[i],
        "price": generate_price()
    }
    destination.append(listing)

  # return sights
  
  outer.append(destination)

  destination = []
  for i in range (5,10):
    listing = {
        "sights": sights[i],
        "description": description[i],
        "links": links[i],
        "images": images[i],
        "price": generate_price()
    }
    destination.append(listing)

  outer.append(destination)
  destination = []
  for i in range (10,15):
    listing = {
        "sights": sights[i],
        "description": description[i],
        "links": links[i],
        "images": images[i],
        "price": generate_price()
    }
    destination.append(listing)
  outer.append(destination)

  return outer
# print(getAttraction("Toronto"))
# links = 
# descriptions = 
# pricing = 
#get destination 
#check yelp review of each destination and pick
#budget algo, figure out the price of the attraction

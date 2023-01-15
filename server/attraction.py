from serpapi import GoogleSearch
import requests

GoogleSearch.SERP_API_KEY = "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9"

def getAttraction():
  # location = keywords[0];
  # need to grab the keyword array from kewords.py
  location = "toronto"
  # keywords[0]

  params = {
    "engine": "google",
    "q": "Top sights in " + location, 
    #change toronto to location after testing
    "location": location,
    "api_key": "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9",
    "num":5
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
    
  print(images)
  return(sights, description, links)
  # return sights

getAttraction()
  
# links = 
# descriptions = 
# pricing = 
#get destination 
#check yelp review of each destination and pick
#budget algo, figure out the price of the attraction

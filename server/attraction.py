from serpapi import GoogleSearch
GoogleSearch.SERP_API_KEY = "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9"
location = input ("Enter city: ")

params = {
  "engine": "google",
  "q": "Top sights in " + location,
  "location": location,
  "api_key": "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9"
}

search = GoogleSearch(params)
results = search.get_dict()
top_sights = results["top_sights"]

print (results)
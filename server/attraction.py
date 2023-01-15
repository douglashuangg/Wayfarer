from serpapi import GoogleSearch
GoogleSearch.SERP_API_KEY = "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9"
location = input ("Enter city: ")

params = {
  "engine": "google",
  "q": "Top attractions in " + location,
  "location": location,
  "api_key": "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9"
}

search = GoogleSearch(params)
results = search.get_dict()
sights = results.get("top_sights").get("sights")

print (sights)
from serpapi import GoogleSearch

params = {
  "q": "Niagara falls, hours of operations",
  "location": "Niagara Falls, Ontario, Canada",
  "hl": "en",
  "gl": "ca",
  "google_domain": "google.ca",
  "api_key": "344a2272107bc37f6bb8abf4dad08e5b64c50d95144a506a8415377f25e365f9"
}

search = GoogleSearch(params)
results = search.get_dict()

hoursofoperation =  [sight.get("title") for sight in results.get("top_sights").get("sights")]
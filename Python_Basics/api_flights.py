import requests

# GET request example
response = requests.get("https://flightapi.com/flights?source=NYC&destination=LAX&date=2022-04-15")
print(response.json())

# POST request example
data = {
    "source": "JFK",
    "destination": "LHR",
    "date": "2022-07-01",
    "passengers": 2,
    "class": "business"
}
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
response = requests.post("https://flightapi.com/bookings", json=data, headers=headers)
print(response.json())

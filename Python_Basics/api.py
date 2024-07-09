import requests

# Make an API request to the OpenWeatherMap API
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+input("City: ")+'&appid=5cf3a96718521eabbe985b47e198c8a9')

# Check if the request was successful
if response.status_code == 200:
    # Print the response content (which contains the weather data)
    data = response.json()
    print(data)
    print((data['main']['temp']-273.15)*1.8+32)
else:
    # Print an error message
    print('Error: Unable to fetch weather data.')
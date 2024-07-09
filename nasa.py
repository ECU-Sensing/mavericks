import requests

def get_nasa_apod(api_key):
    # Define the URL for the NASA APOD API endpoint
    url = "https://api.nasa.gov/planetary/apod"
    
    # Define the parameters for the GET request
    params = {
        'api_key': api_key
    }
    
    # Make the GET request to the NASA API
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Print the title and URL of the image
        print("Title:", data.get("title"))
        print("Date:", data.get("date"))
        print("URL:", data.get("url"))
        print("Explanation:", data.get("explanation"))
    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code, response.text)

# Replace 'DEMO_KEY' with your actual NASA API key
api_key = "s9PWcKn8o7DtIxOYaSCy7u83SYd6t2vUyErACf5u"

get_nasa_apod(api_key)

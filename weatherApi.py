import requests

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

headers = {
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
    'x-rapidapi-key': "da47948ae8msh9794007666c8d7cp14d407jsn152175517c18",
    'accept': "application/json"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
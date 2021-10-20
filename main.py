import requests
import base64
import json
import random
import os


from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
CLIENT_ACCESS_TOKEN = os.getenv('CLIENT_ACCESS_TOKEN')

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': f'Bearer {access_token}'
}
artist = ['5j4HeCoUlzhfWtjAfM1acR',
          '0Y5tJX1MQlPlqiwlOH1tJY', '2h93pZq0e7k5yf4dywlkpM']
ran = random.choice(artist)

IDD = ran
BASE_URL = f'https://api.spotify.com/v1/artists/{IDD}/top-tracks?market=US'

r = requests.get(BASE_URL,
                 headers=headers)
top = r.json()

print(r.status_code)

toptrack = top["tracks"][1]["name"]
print(toptrack)

topurl = top["tracks"][1]["preview_url"]
print(topurl)
names = top["tracks"][1]["artists"][0]["name"]
print(names)
imageurl = top["tracks"][1]["album"]["images"][0]["url"]
print(imageurl)


# genius
Client_token = os.getenv("CLIENT_ACCESS_TOKEN")

BASE_URL2 = f'https://api.genius.com/search'
headers = {
    "Authorization": f"Bearer {CLIENT_ACCESS_TOKEN}"
}
params = {'q': f"artist+toptrack"
          }

lol = requests.get(BASE_URL2,
                   params=params,
                   headers=headers)
url = lol.json()
songurl = url["response"]["hits"][0]["result"]["url"]
print(songurl)

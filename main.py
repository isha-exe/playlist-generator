import requests

# SETTINGS 
endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "BQApNV40h3GqiXHqBwqZRQ0QiBMGEU8RIMvBPu8_LT6To9idFZwX3kH3eEqCenQX96BNxlOvEugdX6k0yfTEbFz1bYb6h1dmi3H7qAe66toa9fmun105-JotnHWieWI2oiVWhFeIEWqmhH1PtuCIriVfM49tU0M"
user_id = "	v6bnl5o8zfigxuk275uy7cyfu"

# OUR FILTERS
limit=10
market="US"
seed_genres="indie"
target_danceability=0.9
uris = [] 
seed_artists = '0XNa1vTidXlvJ2gHSsRi4A'
seed_tracks='55SfSsxneljXOk5S3NVZIW'

# PERFORM THE QUERY
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'
query += f'&seed_artists={seed_artists}'
query += f'&seed_tracks={seed_tracks}'

response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()

print('Recommended Songs:')
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

    
# CREATE A NEW PLAYLIST

import requests
import json 

endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "Indie bands like Franz Ferdinand and Foals but using Python",
          "description": "My first programmatic playlist, yooo!",
          "public": False
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

url = response.json()['external_urls']['spotify']
print(response.status_code)
# FILL THE NEW PLAYLIST WITH THE RECOMMENDATIONS

playlist_id = response.json()['id']

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

print(response.status_code)
201
print(f'Your playlist is ready at {url}')
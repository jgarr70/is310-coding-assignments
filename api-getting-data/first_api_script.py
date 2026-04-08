import os
import requests
from rich import print as rprint


## LOTR API
#
# api_key = os.environ['THE_ONE_API_KEY']

# url = 'https://the-one-api.dev/v2/character'

# authorization_headers = {
#     'Authorization': 'Bearer ' + api_key
# }

# response = requests.get(url, headers=authorization_headers)
# print(response.status_code)

# # print(response.json())
# # for character in response.json()['docs']:
# #     if character['name'] == 'Galadriel':
# #         print(character)

# url = 'https://the-one-api.dev/v2/character?name!=Galadriel&race=Elf'
# response = requests.get(url, headers=authorization_headers)
# print(f"Total number of elves besides Galadriel: {response.json()['total']}")


# import apikey
# import os

# apikey.save("EUROPEANA_API_KEY", "ndismanswa")
# europeana_api_key = apikey.load("EUROPEANA_API_KEY")
# os.environ['EUROPEANA_API_KEY'] = europeana_api_key

## Europeana API


import os
from dotenv import load_dotenv

# This looks for the .env file and loads the variables
load_dotenv()

import pyeuropeana.apis as apis

# response = apis.entity.suggest(
#    text = 'Tolkien',
#    TYPE = 'agent',
# )
# print('tolkien', response)

response = apis.entity.suggest(
   text = 'The Beatles',
   type = 'agent' # Search for people/groups
)

rprint(response['items']) # View first 3 suggestions
for item in response['items'][:4]:
    # 1. Get the main ID
    print(f"ID: {item['id']}")
    
    # 2. Get the Bulgarian name (since it's the only one in prefLabel here)
    main_name = item['prefLabel'].get('bg', 'No Name')
    print(f"Main Name: {main_name}")
    
    # 3. Get all the English nicknames and join them with a comma
    en_aliases = item['altLabel'].get('en', [])
    print(f"English Nicknames: {', '.join(en_aliases)}")
    
    # 4. Get the image URL
    image = item['isShownBy']['id']
    print(f"Image Link: {image}")
import os
import requests

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

response = apis.entity.suggest(
   text = 'Tolkien',
   TYPE = 'agent',
)
print('tolkien', response)
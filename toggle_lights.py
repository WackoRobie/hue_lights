#! /usr/env/python

import requests
import json

URL = "http://192.168.188.22/api/2TVMBPdD12TsazTaC474o1mEK5KZODZ8FEsAs199/groups/"


r = requests.get(URL)

response = json.loads(r.text)

for group in response.keys():
    name = response[group]['name']
    state = True if response[group]['state']['all_on'] == 'true' else False
    print(f'Group: {name}:{state}')

#! /usr/env/python

import requests
import json

IP = '192.168.188.22'
USER = '2TVMBPdD12TsazTaC474o1mEK5KZODZ8FEsAs199'
URL = f"http://{IP}/api/2TVMBPdD12TsazTaC474o1mEK5KZODZ8FEsAs199/groups/"

selection = 'groups'

r = requests.get(f"http://{IP}/api/{USER}/{selection}/")

response = json.loads(r.text)

for group in response.keys():
    name = response[group]['name']
    state = True if response[group]['state']['all_on'] == 'true' else False
    print(f'Group: {name}:{state}')

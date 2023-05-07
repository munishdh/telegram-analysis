import json
import pprint

json_filename = 'channel_messages.json'

with open(json_filename, encoding='utf-8') as json_file:
    data = json.load(json_file)

for item in data:
    if item.get('message'):
        if 'Alert for ST COMBO HTF' in item['message']:
            print(item['message'])
#

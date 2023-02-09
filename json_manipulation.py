# program on how json can be processed

import json

data = '''[
    {"id":"10",
    "name":"Leo",
    "position":"forward"},

    {"id":"4",
    "name":"Ramos",
    "position":"defence"}
]'''

players = json.loads(data)
print("player count:",len(players))

for player in players:
    print('name: ',player["name"])
    print('jerser_number: ',player['id'])
    print('plays: ',player['position'])
import json
# A list that contains two dictionaries.
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)     #Deserialize data (whether info is a list or a dict depends on the data input defined.)
print('User count: ', len(info))

for i in info:
    print('Name: ', i['name'])
    print('ID', i['id'])
    print('Attr', i['x'])


import json

x = '{"firstName": "tester", "lastName": "tester", "city": "Vilnius", "age": "24"}'

# parse x:
y = json.loads(x)

print (y["firstName"])
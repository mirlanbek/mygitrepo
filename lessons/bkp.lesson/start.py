# import argparse

# parser = argparse.ArgumentParser(description="An argparse example")

# parser.add_argument('action', help='The action to take (e.g. install, remove, etc.)')
# parser.add_argument('foo-bar', help='Hyphens are cumbersome in positional arguments')

# args = parser.parse_args()

# if args.action == "install":
#     print("You asked for installation")
# else:
#     print("You asked for something other than installation")

#The following do not work:
 
# But this works:
#print(getattr(args, 'foo-bar'))

import json
book = {}
book['tom'] = {

    'name': 'tom',
    'address': '990 Gina Way, Aloha',
    'phone': 503212112

}
book['tokon'] = {

    'name': 'tokon',
    'address': '990 Perrie dr, Elk Grove Vilage',
    'phone': 7733669911

}

p= json.dumps(book)
print(type(p))

with  open('test.json','w') as jsonFile:
    jsonFile.write(p)

with open("test.json",'r') as jsonFile:
    outRead=jsonFile.read()
 
load_json = json.loads(outRead)

print(load_json)
print(type(load_json))

print(  load_json['tokon']['address'])

f = load_json['tokon']
for i,k in f.items():
    print(i,k)






















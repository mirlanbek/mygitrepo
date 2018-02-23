import json
# Ishtebese startka copy kylypsan ishteit (bul filedyn locationu tuura emes)
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
f = load_json['tokon']
for i,k in f.items():
    print(i,k)
}


p= json.dumps(book)
print(p)
print(type(p))                          ### string

with  open('test.json','w') as jsonFile:
    jsonFile.write(p)

with open("test.json",'r') as jsonFile:
    outRead=jsonFile.read()
 
load_json = json.loads(outRead)

# print(load_json)

# print(type(load_json))

# print(  load_json['tokon']['address'])

f = load_json['tokon']
for i,k in f.items():
    print(i,k)

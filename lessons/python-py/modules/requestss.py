import requests

# GET method

payload = {'page': 2, 'count': 25}

r = requests.get("https://httpbin.org/get", params=payload)

print(r.url)

print(r.status_code)

#POST method
payload = {'username': 'miki', 'password': 'pass123'}

r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

# r.json()

r_dict = r.json()
print(r_dict['form'])

# authenticate

r = requests.get("https://httpbin.org/basic-auth/miki/pass123", auth=('miki', 'pass123'))
print(r.text)



import requests

r = requests.get('http://jservice.io/api/random?count=5')

print(r.json()[0]['question'])
import requests
from pprint import pprint
url=('http://api.open-notify.org/astros.json')
information_about_astronauts = requests.get(url)
pprint(information_about_astronauts.json())

print(information_about_astronauts.json()['number'])
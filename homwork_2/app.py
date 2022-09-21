from flask import Flask
from faker import Faker
import requests

app = Flask(__name__)


@app.route('/', methods=['get'])
def index():
    return 'Hello, this is my first project!'


@app.route('/generate-users', methods=['get', 'post'])
def user_generator():
    name = Faker('uk_UA')
    for _ in range(100):
        return name.first_name(), '-', name.email()


@app.route('/space', methods=['get'])
def astro():
    url = ('http://api.open-notify.org/astros.json')
    information_about_astronauts = requests.get(url)
    space = str(information_about_astronauts.json()['number'])
    return f'Number of astronauts at the moment is {space} people  '


if __name__ == '__main__':
    app.run(debug=True)

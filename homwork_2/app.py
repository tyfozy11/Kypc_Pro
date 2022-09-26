from flask import Flask, render_template, request
from faker import Faker
import requests

app = Flask(__name__)
name = Faker('uk_UA')


@app.route('/', methods=['get'])
def index():
    return 'Hello, this is my first project!'


@app.route('/requirements', methods=['get'])
def requirements():
     while open('requirements.txt', 'r') as file:
        return file


@app.route('/generate-users', methods=['get', 'post'])
def user_generator():
    generation_result = {}

    if request.method == 'POST':
        users = ""
        number_of_users = int(request.form['number_of_users'])
        if not int(request.form['number_of_users']):
            number_of_users = 100

        for fake in range(number_of_users):
            users += f'\n\n{name.first_name()} - {name.email()}\n'
            generation_result['users'] = users
    return render_template('user_generator.html', **generation_result)


@app.route('/space', methods=['get'])
def astro():
    url = ('http://api.open-notify.org/astros.json')
    information_about_astronauts = requests.get(url)
    if information_about_astronauts.status_code == 200:
        return f"Number of astronauts at the moment is {str(information_about_astronauts.json()['number'])} people"


if __name__ == '__main__':
    app.run(debug=True)

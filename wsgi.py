import json

from flask import Flask, render_template, jsonify, request
from data.service_data import cities

app = Flask(__name__)


def get_cities():
    return cities


def set_city(city_object):
    cities.append(city_object)
    return get_cities()


def del_city(id):
    for city in cities:
        if city['id'] == id:
            city_name = city['name']
            cities.remove(city)
            return f'City "{city_name}" successfully deleted'
    return f'City with id: {id} not found'


@app.route('/', methods=['GET'])
@app.route('/hello', methods=['GET'])
def hello():
    cities = get_cities()
    return render_template('hello.html', cities=cities, title='Hello Page')


@app.route('/cities', methods=['GET'])
def citiesAll():
    cities = get_cities()
    return jsonify({'cities': cities})


@app.route('/city/<int:index>', methods=['GET'])
def cityOne(index):
    cities = get_cities()
    try:
        result = cities[index]
    except IndexError:
        result = f'No such city index, number of available cities is: {len(cities)}'
    return result


@app.route('/city', methods=['POST'])
def city():
    city_object = {'id': int(request.form['id']),
                   'name': request.form['name'],
                   'zip_code': request.form['zip_code']}
    is_duplicated  = any(city_object['id'] == city['id'] for city in get_cities())
    result = get_cities() if is_duplicated else set_city(city_object)
    return jsonify({'cities': result})


@app.route('/city/<int:id>', methods=['DELETE'])
def delCity(id):
    result = del_city(id)
    return result

@app.route('/health/check', methods=['GET', 'POST', 'PUT'])
def health_check():
    return jsonify({'message': 'It works!'})


@app.route('/<string:name>', methods=['GET'])
def personal_hello(name: str):
    return f'<h1>Hello {name.capitalize()}! This in my first Flask app:)</h1>'

@app.route('/help', methods=['GET'])
def help():
    return render_template('help.html', title='Help Page')

if __name__ == "__main__":
    app.run()


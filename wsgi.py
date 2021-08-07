from flask import Flask, render_template
from data.service_data import cities

app = Flask(__name__)


def get_cites():
    return cities


@app.route('/')
@app.route('/hello')
def hello():
    cites = get_cites()
    return render_template('hello.html', cites=cites, title='Hello Page')


@app.route('/<string:name>')
def personal_hello(name: str):
    return f'<h1>Hello {name.capitalize()}! This in my first Flask app:)</h1>'

@app.route('/help')
def help():
    return render_template('help.html', title='Help Page')

if __name__ == "__main__":
    app.run()


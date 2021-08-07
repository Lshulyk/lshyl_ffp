from flask import Flask, render_template

app = Flask(__name__)


def get_cites():
    return [
        {'id': 1,
         'name': 'Lviv',
         'zip_code': 79007},
        {'id': 2,
         'name': 'Dolyna',
         'zip_code': 77522},
        {'id': 1,
         'name': 'Ivano-Frankivs',
         'zip_code': 76026}
    ]


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


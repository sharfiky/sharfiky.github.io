from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/station', methods=['GET', 'POST'])
def station():
    states = [
        {'number': '1',
         'name': 'Rotor',
         'consist': '20'},
        {'number': '2',
         'name': 'Differ',
         'consist': '30'},
        {'number': '3',
         'name': 'Rotor',
         'consist': '10'}
    ]
    return render_template('station.html',
                           states=states)


@app.route('/position', methods=['GET', 'POST'])
def position():
    states = [
        {'name': 'Station 1',
         'percent': '60'},
        {'name': 'Station 2',
         'percent': '50'},
        {'name': 'Station 5',
         'percent': '40'},
        ]
    return render_template('position.html',
                           states=states)


if __name__ == '__main__':
    app.run()

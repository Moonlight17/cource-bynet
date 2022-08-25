from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/test/')
def test_func():  # put application's code here
    return 'OLOLO!'


if __name__ == '__main__':
    app.run()

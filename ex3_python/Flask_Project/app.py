import flask, requests, json

# from flask import Flask

app = flask.Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# Basic routing
@app.route('/route/')
def info():  # put application's code here
    return 'Basic routing complite!'

@app.route('/parametrs/<int:age>/')
def age_func(age):
    return 'Your age => %f' % age

@app.route('/headers')
def json_with_headers():
    if flask.request.args.get('name'):
        name = flask.request.args.get('name')
    else:
        name = "sergei"
    url = "https://api.nationalize.io/?name="+name
    response = requests.request("GET", url)
    resp = flask.make_response(json.dumps(response.text))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['content-type'] = "application/json"
    return resp
    # response = app.response_class(
    #         response=flask.json.dumps(data),
    #         status=200,
    #         mimetype='application/json'
    #     )



if __name__ == '__main__':
    app.run()

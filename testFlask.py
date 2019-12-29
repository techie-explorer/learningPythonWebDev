from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    return "Hello Farhan!"


@app.route('/getDetails')
def get_details():
    return {
        'name': "Farhan",
        'age': 21
    }


if __name__ == '__main__':
    app.run()

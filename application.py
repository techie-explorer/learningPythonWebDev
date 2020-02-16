from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    return 'Hello Farhan! This is direct integration from GitHub' \
           '<div style="height=50px; width=50px; background-color=red"></div>'


if __name__ == '__main__':
    app.run()

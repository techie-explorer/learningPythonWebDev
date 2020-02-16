from flask import Flask

app = Flask(__name__)


def render_homepage():
    render_greeting_text = """
    <div style="height: 100px; width: 100px; background-color: 'red'">
        Hello Welcome to Azure Python Flask Application
    </div>
    """
    return render_greeting_text


@app.route('/')
def say_hello():
    return render_homepage()


def render_details_page():
    details_page = "hahahha"
    return details_page


@app.route('details')
def say_hello():
    return render_details_page()


if __name__ == '__main__':
    app.run()

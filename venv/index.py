from flask import Flask


app = Flask(__name__)


# Adapted from https://github.com/rus19023/vercel_deploy.git


@app.route('/')
def home():
    return 'Home Page Route - nice work Andrew!!!'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text
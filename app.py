from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Home')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About')


if __name__ == '__main__':
    app.run(debug=True)
# creating a simple website using Flask

from flask import Flask

# create an instance of Flask class
app = Flask(__name__)

# Decorators - defining weblinks
@app.route('/')
# view to be returned when home page is called
def home():
    return '<h1> Welcome to Jays page </h1>'

@app.route('/about')
def about():
    return '<h1> About Us page</h1>'

# dynamic routing
@app.route('/user/<name>')
def user(name):
    return '<h1> This is user {} </h1>' .format(name)

if __name__ == "__main__":
    app.run(debug=True)


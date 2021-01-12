# Code written by Jerin Rajan on 12th Jan 2020

from flask import Flask

# creating an instance of Flask application
app = Flask(__name__)

# Decorators
@app.route('/')
def index():
    return ('<h1> Welcome! Go to puppy_latin/name to see name in puppy latin </h1>')

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1:] == 'y':
        latin_name=name[0:-1]+'iful'

    else:
        latin_name=name+'y'

    return ('Hi {} ! Your puppy latin name is {} '.format(name, latin_name))

if __name__ == '__main__':
    app.run(debug=True)


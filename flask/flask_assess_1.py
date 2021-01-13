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
        latin_name=name[:-1]+'iful'

    else:
        latin_name=name+'y'

    return ('<h1> Hi {} ! Your puppy latin name is {} </h1>'.format(name, latin_name))

@app.route('/puppy_name_caps/<name>')
def puppy_name_caps(name):
    name_caps = name.upper()

    return ('the puppy name in caps is: {}'.format(name_caps))


if __name__ == '__main__':
    app.run(debug=True)


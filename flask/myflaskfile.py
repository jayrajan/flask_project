from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Jay'
    user_logged_in = False
    return render_template('index.html', name=name, user_logged_in=user_logged_in)

if __name__ == "__main__":
    app.run(debug=True)

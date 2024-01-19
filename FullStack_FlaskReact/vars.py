from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html', list_of_names=['Chris', 'John'])


if __name__ == '__main__':
    app.run(debug=True)
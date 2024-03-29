from flask import Flask, render_template, request, redirect, url_for
from forms import Todo

app = Flask(__name__)
app.config['SECRET_KEY'] ='password'

@app.route('/', methods=['GET', 'POST'])
def hello_world():

    request_method = request.method
    if request.method == 'POST':
        first_name = request.form['first_name'] 
        return redirect(url_for('first_name', first_name=first_name))
    return render_template('hello.html', request_method=request_method)

@app.route('/first_name/<string:first_name>')
def name(first_name):
    return f'{first_name}'

@app.route('/todo', methods=['GET'])
def todo():
    todo_form = Todo()
    return render_template('todo.html', form=todo_form)

if __name__=='__main__':
    app.run(debug=True)
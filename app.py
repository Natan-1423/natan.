@app.route('/register_submit', methods=['POST'])
def register_submit():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    birthday = request.form['birthday']
    
    # Process the data (save to database, validate, etc.)
    
    return 'Registration successful'
flask run
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/register_submit', methods=['POST'])
def register_submit():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # Save user data logic here

    # After successful registration
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from models import User
from database import db_session, init_db

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', user='Kirill')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form.get('username')
        password_1, password_2 = request.form.get('password_1'), request.form.get('password_2')
        if password_1 == password_2:
            user_data = User(username, password_1, password_2)
            db_session.add(user_data)
            db_session.commit()
            return redirect(url_for('home'))
        return "<h1> Password does not match </h1>"
    return render_template('registration.html')


if __name__ == "__main__":
    app.run()

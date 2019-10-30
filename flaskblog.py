from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import datetime
app = Flask(__name__)

app.config['SECRET_KEY'] = '432798b5b6902e2bf5e1f02f993d824c'

posts = [{
    '_id': 0,
    'name': 'Bob',
    'dob': datetime.datetime(1996, 11, 12, 11, 14),
    'email': 'bob@gmail.com',
    'status': 0
}, {
    '_id': 1,
    'name': 'Mason',
    'dob': datetime.datetime(1996, 11, 12, 11, 14),
    'email': 'mason@gmail.com',
    'status': 1
}]


@app.route('/')  #'/' is root page
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/about')
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)

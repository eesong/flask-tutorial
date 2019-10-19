from flask import Flask, render_template, url_for
import datetime
app = Flask(__name__)

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


@app.route('/about')
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)

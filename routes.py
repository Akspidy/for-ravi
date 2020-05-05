from flask import url_for, render_template, flash, redirect
from firstapp import app, db, bcrypt
from firstapp.forms import RegistrationForm, LoginForm
from firstapp.models import User,Post



posts = [
    {
        'author': 'Aman Kumar',
        'title': 'Blog Post 1',
        'content': 'first blog content',
        'date_posted': 'April 26,2020'
    }, {
        'author': 'Aashu Kumar',
        'title': 'Blog Post 2',
        'content': 'second blog content',
        'date_posted': 'April 27,2020'
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

from flask import render_template, url_for, flash, redirect
from blog_app import app
from blog_app.forms import RegistrationForm, LoginForm
from blog_app.models import User, Post

posts = [
    {
        'author': 'John Doe',
        'title': 'Post 1',
        'content': 'Post 1 content',
        'date': 'May 3, 1997'
    },
    {
        'author': 'Betty Doe',
        'title': 'Post 2',
        'content': 'Post 2 content',
        'date': 'May 5, 1997'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed!. Check your credentials!', 'danger')
    return render_template('login.html', title='login', form=form)
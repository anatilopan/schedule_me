from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'joe'}
    return render_template('base.html', title='Home', user=user)

@app.route('/myschedule')
def myschedule():
    user = {'username': 'joe'}
    periods = [
        {
        'name': 'Floating Hour',
        'description': 'Breakfeast or something',
        'starting_hour': '10',
        'starting_minute': '00',
        'ending_hour':'11',
        'ending_minute':'00',
        },
        {
        'name': 'Floating Hour',
        'description': 'Breakfeast or something',
        'starting_hour': '10',
        'starting_minute': '00',
        'ending_hour':'11',
        'ending_minute':'00',
        }
    ]
    return render_template('myschedule.html', title='My Schedule', user=user, periods=periods)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login required for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for(index))
    return render_template('login.html', title='Sign In', form=form)
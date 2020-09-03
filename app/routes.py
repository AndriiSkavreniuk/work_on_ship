from flask import render_template, flash, redirect, url_for, request
from app.forms import MeinForm
from app import app, db
from app.models import User, Admin
from flask_login import logout_user, login_user


from app.forms import LoginForm



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MeinForm()
    if request.method == 'POST' and form.validate_on_submit():
        order = User(first_name=form.first_name.data,
                     last_name=form.last_name.data,
                     email=form.email.data,
                     number='+380' + form.number.data)
        db.session.add(order)
        db.session.commit()
        flash('Вашу заявку прийнято.')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(admin=form.admin.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(admin)
        return redirect(url_for('admin.index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

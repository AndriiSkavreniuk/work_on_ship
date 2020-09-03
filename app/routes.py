from flask import render_template, flash, redirect, url_for, request
from app.forms import MeinForm
from app import app, db
from app.models import User

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MeinForm()
    if request.method == 'POST' and form.validate_on_submit():
        order = User(first_name=form.first_name.data,
                     last_name=form.last_name.data,
                     email=form.email.data,
                     number='+380'+form.number.data)
        db.session.add(order)
        db.session.commit()
        flash('Вашу заявку прийнято.')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
from application import app
from collections import User
from flask import session, render_template, redirect, flash
from forms import SignupForm
from werkzeug.security import generate_password_hash

@app.route('/signup', methods=['POST','GET'])
def signup():
    form = SignupForm()
    if session.get('logged_in'):
        return redirect(url_for('index'))
    if form.validate_on_submit():
        if form.password.data == form.password2.data:
            pw_hash = generate_password_hash(form.password.data)
            user = User(email = form.email.data, alias = form.alias.data, password = pw_hash)
            try:
                user.save()
                return redirect(url_for("login"))
            except Exception, e:
                print('exception %s' % str(e))
                if 'Invalid Mail-address' in str(e):
                    flash('Invalid email')
    return render_template('signup.html', form = form)

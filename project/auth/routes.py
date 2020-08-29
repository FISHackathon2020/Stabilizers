from flask import(
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from project import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

#Should be able to create student and representative acounts
@auth.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        first_name = request.form['first']
        last_name = request.form['last']
        email = request.form['email']
        password = request.form['password']
        error = None
        id = db.execute('SELECT id FROM user WHERE email = ?', (email,))

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif id is not None:
            error = 'Email %s is already registered.'.format(email)

        if error is None:
            db.execute(
                'INSERT INTO user (email, password, first, last)'
                '   values (?, ?, ?, ?)',
                (email, password, first_name, last_name)
            )
            if email[-3:] == 'edu':
                school = email[ email.find('@')+1 : email.find('.') ]
                db.execute(
                    'INSERT INTO student (id, school) values (?, ?)',
                    (id, school)
                )

        flash(error)
    return render_template('auth/register.html')


@auth.route('/login')
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None
        user = db.execute(
            'SELECT *  FROM user WHERE email = ?', (email,)
        )

    if user is None or not user['password', password]:
        error = 'Incorrect email or password.'

    if error is None:
        session.clear()
        session['user_id'] = user['id']
        return redirect(url_for('index'))

    flash(error)
    return render_template('auth/login.html')

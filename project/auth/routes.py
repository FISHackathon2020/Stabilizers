from flask import(
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from project import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

#Should be able to create student and representative acounts
@auth.route('/register', methods=('POST','GET'))
def register():
    if request.method == 'POST':
        first_name = request.form['first']
        last_name = request.form['last']
        email = request.form['email']
        password = request.form['password']
        error = None
        id = db.engine.execute('SELECT id FROM users WHERE email = ?', (email,)).fetchone()

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif id is not None:
            error = 'Email {} is already registered.'.format(email)

        if error is None:
            db.engine.execute(
                'INSERT INTO users (email, password, first_name, last_name)'
                '   values (?, ?, ?, ?)',
                (email, password, first_name, last_name)
            )
            if email[-3:] == 'edu':
                school = email[ email.find('@')+1 : email.find('.') ]
                db.engine.execute(
                    'INSERT INTO students (id, school) values (?, ?)',
                    (id, school,)
                )

            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@auth.route('/login', methods=('POST', 'GET'))
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		error = None
		user = db.engine.execute('SELECT *  FROM users WHERE email = ?', (email,)).fetchone()

		if user is None or user['password'] != password:
			error = 'Incorrect email or password.'

		if error is None:
			session.clear()
			session['user_id'] = user['id']
			return redirect(url_for('social.feed'))

		flash(error)
	return render_template('auth/login.html')

@auth.before_app_request
def load_logged_in_user():
	user_id = session.get('user_id')

	if user_id is None:
		g.user = None
	else:
		g.user = db.engine.execute(
			'SELECT * FROM users WHERE id = ?', (user_id,)
		).fetchone()

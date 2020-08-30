from flask import(
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from project import db

social = Blueprint('social', __name__)

def get_user(id):
    user = db.engine.execute(
        'SELECT id, first_name, last_name, email, bio'
        '   FROM users u'
        '   WHERE u.id = ?',
        (id,)
    ).fetchone()

    if user is None:
        abort(404, "User doesn't exist.")

    return user

def get_student(id):
    student = db.engine.execute(
        'SELECT school, major'
        '   FROM students s JOIN users u ON s.id = u.id'
        '   WHERE u.id = ?',
        (id,)
    ).fetchone()

    return student

def get_representative(id):
    representative = db.engine.execute(
        'SELECT company'
        '   FROM representatives r JOIN users u ON r.id = u.id'
        '   WHERE u.id = ?',
        (id,)
    ).fetchone()

    return representative

@social.route('/portfolio/<int:id>', methods=['GET'])
def portfolio(id):
    user = get_user(id)
    student = get_student(id)
    representative = get_representative(id)

    return render_template('social/portfolio.html', user=user, student=student, representative=representative)

@social.route('/', methods=['GET'])
def feed():
    posts = db.engine.execute(
        'SELECT p.id, title, body, created, author_id, first_name, option'
        '   FROM posts p JOIN users u ON p.author_id = u.id'
        '   ORDER BY created DESC'
    ).fetchall()

    return render_template('social/feed.html', posts=posts)

@social.route('/ideas/<int:id>', methods=['GET'])
def ideas(id):
    posts = db.engine.execute(
        'SELECT p.id, title, body, created, author_id, first_name, option'
        '   FROM posts p JOIN users u ON p.author_id = u.id WHERE option = ?',('option',)
    ).fetchall()

    return render_template('social/feed.html', posts=posts)

@social.route('/experiences/<int:id>', methods=['GET'])
def expereinces(id):
    posts = db.engine.execute(
        'SELECT p.id, title, body, created, author_id, first_name, option'
        '   FROM posts p JOIN users u ON p.author_id = u.id WHERE option = ?',('experience',)
    ).fetchall()

    return render_template('social/feed.html', posts=posts)

@social.route('/opportunities/<int:id>', methods=['GET'])
def opportunities(id):
    posts = db.engine.execute(
        'SELECT p.id, title, body, created, author_id, first_name, option'
        '   FROM posts p JOIN users u ON p.author_id = u.id WHERE option = ?',('opportunity',)
    ).fetchall()
    return render_template('social/feed.html', posts=posts)

@social.route('/create', methods=['POST','GET'])
def create():
    student = get_student(g.user['id'])
    representative = get_representative(g.user['id'])
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        option = request.form['options']
        error = None

        if not title:
            error = 'Title is required'

        if error is not None:
                flash(error)
        else:
            db.engine.execute(
                'INSERT INTO posts (title, body, author_id, option)'
                '   VALUES (?, ?, ?, ?)',
                (title, body, g.user['id'], option)
            )

            return redirect(url_for('social.feed'))

    return render_template('social/create.html', student=student, representative=representative)

from flask import(
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from project import db

social = Blueprint('social', __name__)

def get_user(id):
        user = db.execute(
        'SELECT first, last, email, bio'
        '   FROM user u'
        '   WHERE u.id = ?',
        (id,)
    ).fetchone()

    if user is None:
        abort(404, "User doesn't exist.")

    return user

def get_student(id):
        student = db.execute(
        'SELECT school, major'
        '   FROM student s JOIN user u ON s.id = u.id'
        '   WHERE u.id = ?',
        (id,)
    ).fetchone()

    return student

def get_representative(id):
        representative = db.execute(
        'SELECT company'
        '   FROM representative r JOIN user u ON r.id = u.id'
        '   WHERE u.id = ?',
        (id,)
    ).fetchone()

    return representative

@social.route('/int:id/portfolio', methods=('GET'))
def portfolio(id):
    user = get_user(id)
    student = get_student(id)
    representative = get_representative(id)

    return render_template('social/portfolio.html', user=user, student=student, representative=representative)

@social.route('/', methods=('GET'))
def feed():
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        '   FROM post p JOIN user u ON p.author_id = u.id'
        '   ORDER BY created DESC'
    ).fetchall()

    return render_template('social/feed.html', posts=posts)

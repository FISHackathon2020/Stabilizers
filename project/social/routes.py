from flask import(
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app import db

bp = Blueprint('blog', __name__)

def get_student(id):
        student = db.execute(
        'SELECT s.id, first, last, school'
        '   FROM student s JOIN user u ON s.id = u.id'
        '   WHERE u.id = ?',
        (id,)
    ).fetchone()

    if student is None:
        abort(404, "Student doesn't exist."

    return post

@bp.route('/int:id/portfolio', methods=('GET'))
def portfolio(id):
    student = get_student(id)



    return render_template('social/portfolio', name=name)

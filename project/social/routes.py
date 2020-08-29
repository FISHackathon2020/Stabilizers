from flask import(
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from project import db

social = Blueprint('social', __name__, url_prefix='/social')

@social.route('/example', methods=('POST', 'GET'))
def example_route():
    pass
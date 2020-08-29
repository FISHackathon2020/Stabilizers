from app import db
from models.auth.user import User

class Student(User):

    # __tablename__ = 'students'

    id = db.Column(db.Integer, db.ForeignKey('user_table.id'), primary_key=True)
    school = db.Column(db.String(200), unique=False, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }
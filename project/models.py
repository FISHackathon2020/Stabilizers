from project import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    middle_name = db.Column(db.String(100), unique=False, nullable=True)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    suffix = db.Column(db.String(3), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(42), unique=False, nullable=False)
    type = db.Column(db.String(20), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user_table',
        'polymorphic_on': type
    }

class Student(User):

    # __tablename__ = 'students'

    id = db.Column(db.Integer, db.ForeignKey('user_table.id'), primary_key=True)
    school = db.Column(db.String(200), unique=False, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }

class Representative(User):

    # __tablename__ = 'representatives'

    id = db.Column(db.Integer, db.ForeignKey('user_table.id'), primary_key=True)
    company = db.Column(db.String(200), unique=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'representative'
    }
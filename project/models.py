from project import db
import datetime

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    middle_name = db.Column(db.String(100), unique=False, nullable=True)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    suffix = db.Column(db.String(3), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(42), unique=False, nullable=False)
    bio = db.Column(db.String(500), unique=False, nullable=True)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        # 'polymorphic_identity': 'user_table',
        'polymorphic_on': db.case([
            (type == "S", "student"),
            (type == "R", "representative")
        ], else_="representative")
    }

class Student(User):

    __tablename__ = 'students'

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    school = db.Column(db.String(200), unique=False, nullable=True)
    major = db.Column(db.String(200), unique=False, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }

class Representative(User):

    __tablename__ = 'representatives'

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    company = db.Column(db.String(200), unique=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'representative'
    }

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(100), unique=False, nullable=False)
    body = db.Column(db.String(500), unique=False, nullable=False)
    option = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    __mapper_args__ = {
        # 'polymorphic_identity': 'post_table',
        'polymorphic_on': db.case([
            (option == "EXP", "experience"),
            (option == "IDEA", "idea"),
            (option == "OPP", "opportunity")
        ], else_="idea"),
    }

class Experience(Post):

    __tablename__ = 'experiences'

    id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'experience'
    }

class Idea(Post):

    __tablename__ = 'ideas'

    id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'idea'
    }

class Opportunity(Post):

    __tablename__ = 'opportunities'

    id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'opportunity'
    }

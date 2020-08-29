from app import db
from models.auth.user import User

class Representative(User):

    # __tablename__ = 'representatives'

    id = db.Column(db.Integer, db.ForeignKey('user_table.id'), primary_key=True)
    company = db.Column(db.String(200), unique=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'representative'
    }
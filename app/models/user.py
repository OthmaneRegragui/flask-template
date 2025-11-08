from app.extensions import db
from app.utils.crud_mixin import CRUDMixin

class User(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(20), default='user')

    def __repr__(self):
        return f'<User {self.username}>'
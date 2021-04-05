# Python standard
from datetime import datetime

# Local
from config import db


class FirstName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.Date, default=datetime.today().date())

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'is_active': self.is_active,
            'created_at': str(self.created_at.strftime('%d-%m-%Y'))
        }

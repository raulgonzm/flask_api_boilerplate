# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=True)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __repr__(self):
        return '<Category: {} - {}>'.format(self.id, self.name)

    def __str__(self):
        return '<Category: {} - {}>'.format(self.id, self.name)

from helper.database import db

from datetime import datetime

class Event(db.Model):
    __tablename__ = 'Events'
    event_id = db.Column(db.Integer, primary_key=True)
    event_type_id = db.Column(db.Integer)
    predicted_release_date = db.Column(db.DateTime)
    predicted_textual_release_date = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, event_type_id, predicted_release_date=None, \
            predicted_textual_release_date=None):
        self.event_type_id = event_type_id
        self.predicted_release_date = predicted_release_date
        self.predicted_textual_release_date = predicted_textual_release_date

class EventType(db.Model):
    __tablename__ = 'EventTypes'
    event_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

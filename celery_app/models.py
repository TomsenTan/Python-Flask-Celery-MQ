from celery_app import db
import datetime

class  Reminder(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    date = db.Column(db.DateTime(),default=datetime.datetime.now())
    email = db.Column(db.String(50))
    text = db.Column(db.Text())

    def __repr__(self):
        return '<Reminder>'

db.create_all()
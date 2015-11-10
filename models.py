import datetime
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)
    date_deleted = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, state, status, latitude, longitude):
        self.name = name
        self.state = state
        self.status = status
        self.latitude = latitude
        self.longitude = longitude
        self.date_created = datetime.datetime.utcnow()
        self.date_updated = datetime.datetime.utcnow()
        self.date_deleted = None

    def __repr__(self):
        return '<City: %r>' % self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)
    date_deleted = db.Column(db.DateTime, nullable=True)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.date_created = datetime.datetime.utcnow()
        self.date_updated = datetime.datetime.utcnow()
        self.date_deleted = None

    def __repr__(self):
        return '<User: %r %r>' % (self.first_name, self.last_name)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)
    date_deleted = db.Column(db.DateTime, nullable=True)

    def __init__(self, user_id, city_id):
        self.user_id = user_id
        self.city_id = city_id
        self.date_created = datetime.datetime.utcnow()
        self.date_updated = datetime.datetime.utcnow()
        self.date_deleted = None

    def __repr__(self):
        return '<Visit: %r @ %r>' % (self.user.user_id, self.city.city_id)
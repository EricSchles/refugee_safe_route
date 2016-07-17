"""

Here the models for our database is defined.

I am using Postgres, Flask-SQLAlchemy for this application.

For an introduction to Flask-SQLAlchemy check out: http://flask-sqlalchemy.pocoo.org/2.1/
""" 
from app import db

class WayPoints(db.Model):
    __tablename__ = 'waypoints'
    id = db.Column(db.Integer,primary_key=True)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)

    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return repr(self.latitude,self.longitude)
    
        

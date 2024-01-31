from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.String(100), nullable=False)
    mac = db.Column(db.String(100), nullable=False)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    def __repr__(self):
        return f"Client('{self.name}', '{self.ip}', '{self.mac}', '{self.longitude}', '{self.latitude}')"

from flaskr.models import db

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(128))
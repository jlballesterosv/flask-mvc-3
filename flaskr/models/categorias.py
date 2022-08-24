from flaskr.models import db

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(128), unique=True, nullable=False)
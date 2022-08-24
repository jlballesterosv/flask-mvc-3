from flaskr.models import db

class Facturas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    productos = db.relationship('productos', secondary='facturas_productos', back_populates='facturas')

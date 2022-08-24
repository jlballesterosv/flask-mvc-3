from enum import unique
from flaskr.models import db, categorias

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(128), unique=True, nullable=False)
    valor_unitario = db.Column(db.Float(10,8))
    unidad_medida = db.Column(db.String(3), nullable=False)
    cantidad_stock = db.Column(db.Float(10,8))
    categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    facturas = db.relationship('facturas', secondary='facturas_productos', back_populates='productos')
    
    def __init__(self, id, descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria):
        self.id = id
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantidad_stock = cantidad_stock
        self.categoria = categoria
        
    def __repr__(self):
        return f'Productos({self.id}, {self.descripcion}, {self.valor_unitario}, {self.unidad_medida}, {self.cantidad_stock}, {self.categoria})'
    
    def __str__(self):
        return self.descripcion
    
    
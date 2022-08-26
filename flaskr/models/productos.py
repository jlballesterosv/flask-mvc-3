from enum import unique
from flaskr.models import db, categorias
from flaskr.models import *

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(128), unique=True, nullable=False)
    valor_unitario = db.Column(db.Float(10,8))
    unidad_medida = db.Column(db.String(3), nullable=False)
    cantidad_stock = db.Column(db.Float(10,8))
    categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    facturas = db.relationship('facturas', secondary='facturas_productos', back_populates='productos')
    
    
    
def obtener_productos():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria FROM productos")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def obtener_productos_por_id(id):
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria FROM productos WHERE id = {}".format(id))
        productos = cursor.fetchall()
    conexion.close()
    return productos

#def crear_producto(producto):
    

    
    
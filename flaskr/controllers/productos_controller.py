from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template
from flaskr.models import db, productos
# import pymysql

# def obtener_conexion():
#     return pymysql.connect(host='localhost',
#                                 user='root',
#                                 password='',
#                                 db='facturacion1')
    
# def obtener_productos():
#     conexion = obtener_conexion()
#     productos = []
#     with conexion.cursor() as cursor:
#         cursor.execute("SELECT id, descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria FROM productos")
#         productos = cursor.fetchall()
#     conexion.close()
#     return productos

class ProductosController(FlaskController):   
    @app.route("/productos")
    def productos():
        # productos = obtener_productos()
        resultProductos = db.session.query(productos).all()
        for producto in resultProductos:
            print(producto.descripcion)
        return render_template('productos.html', titulo='Gestión de Productos', lista_productos=resultProductos)
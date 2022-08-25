from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template
from flaskr.models import db, categorias, productos, facturas, facturas_productos

class ProductosController(FlaskController):   
    @app.route("/productos")
    def productos():
        resultProductos = productos.obtener_productos()
        return render_template('productos.html', titulo='Gestión de Productos', lista_productos=resultProductos)
    
    @app.route("/crear_producto")
    def crear_producto():
        resultProductos = productos.obtener_productos()
        return render_template('crear_producto.html', titulo='Nuevo Producto')
    

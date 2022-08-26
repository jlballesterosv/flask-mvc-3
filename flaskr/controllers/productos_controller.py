
from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template
from flaskr.models import db, categorias, productos, facturas, facturas_productos

class ProductosController(FlaskController):   
    @app.route("/productos")
    def productos():
        resultProductos = productos.obtener_productos()
        return render_template('productos.html', titulo='Gestión de Productos', lista_productos=resultProductos)
    
    # @app.route("/crear_producto", methods=['POST'])
    # def crear_producto():
    #     if request.method == 'POST':
    #         producto = productos()
    #         producto.id = request.form['id']
    #         producto.descripcion = request.form['descripcion']
    #         producto.valor_unitario = request.form['valor_unitario']
    #         producto.unidad_medida = request.form['unidad_medida']
    #         producto.cantidad_stock = request.form['cantidad_stock']
    #         producto.categoria = request.form['categoria']
    #         if not producto.descripcion:
    #             flash('La descripción es un campo obligatorio')   
    #         elif not producto.valor_unitario:
    #             flash('La descripción es un campo obligatorio')   
    #         else:
    #             return redirect(url_for('index'))    
    #     return render_template('crear_producto.html', titulo='Nuevo Producto')
    

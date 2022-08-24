from flask import Flask
from flaskr.controllers import *

def create_app(config_name):
    app = Flask(__name__, static_folder=None)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database//facturacion.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/facturacion1'
    app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False
    if __name__ == '__main__':
        app.run(debug=True)
    return app


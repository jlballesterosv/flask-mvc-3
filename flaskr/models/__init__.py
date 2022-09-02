from email.mime import image
from flask_sqlalchemy import SQLAlchemy
import flaskr
from flaskr.models import *
import pymysql

db = SQLAlchemy()

def obtener_conexion():
        return pymysql.connect(host='localhost',
                                    user='root', 
                                    password='',
                                    db='facturacion')




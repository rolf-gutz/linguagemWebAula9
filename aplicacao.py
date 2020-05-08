from flask import Flask
import sqlite3

#configuração 

DATABASE ='banco.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__) # Inicializando o modulo 

def conectar_bd():
    return sqlite3.connect(DATABASE)

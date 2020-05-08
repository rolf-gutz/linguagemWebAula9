from aplicacao import app
from aplicacao import conectar_bd
from contextlib import closing

def criar_bd():
    with closing(conectar_bd()) as bd:
        with app.open_resource('esquema.sql') as sql:
            bd.cursor().executescript(sql.read().decode('utf-8'))
        bd.commit()

criar_bd()
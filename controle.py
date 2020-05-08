from aplicacao import app
from flask import render_template
from flask import g
from aplicacao import conectar_bd

@app.before_request
def pre_requesicao():
    g.db = conectar_bd()

@app.teardown_request
def encerrar_requisicao(exception):
    g.db.close()

@app.route('/')
def index():
    sql = '''select usuario,texto from mensagens order by id desc'''
    cur = g.db.execute(sql)
    mensagens = [dict(usuario = usuario , texto = texto)
                    for usuario, texto in cur.fetchall()]
    context = {'titulo':'Página Principal',
    'mensagens': mensagens
    }
    return render_template('index.html',**context)

@app.route('/mensagem')
def mensagem():
    context = {'titulo':'Escrever mensagem'}
    return render_template('mensagem.html',**context)


app.run(debug=True)
from flask import Flask, render_template, request
from rotinas import int_to_Roman, loadDados

app = Flask(__name__)

@app.route('/detalhes/')
def hello_world():  # put application's code here
    cp = request.args.get('cap')
    busca = request.args.get('pesquisaTermo')
    livro = loadDados(cp)
    encontrado = False
    if busca is not None:
        if busca in livro:
            encontrado = True
    else:
        busca = ''
    return render_template('app.html', texto=livro, cp=cp, busca=busca, encontrado=encontrado)

@app.route('/')
def index():
    dados = loadDados()
    return render_template('index.html', dados=dados)

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, url_for
from rotinas import intToRoman, loadDados

app = Flask(__name__)


@app.route('/detalhes/')
def detalhes():  # put application's code here
    cp = request.args.get('cap')
    busca = request.args.get('pesquisaTermo')
    livro = loadDados(cp)
    encontrado = False
    print(busca)
    if busca not in [None, "", '']:
        if busca in livro:
            encontrado = True
    else:
        busca = ''
    return render_template('app.html', texto=livro, cp=cp, busca=busca, encontrado=encontrado)


@app.route('/')
def index():
    dados = loadDados()
    return render_template('index.html', dados=dados)


# @app.route('/<path:dummy>')
# def fallback(dummy=None):
#     return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html')


if __name__ == '__main__':
    app.run()

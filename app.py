from flask import Flask, render_template, request
from rotinas import int_to_Roman, loadDados

app = Flask(__name__)

@app.route('/detalhes/')
def hello_world():  # put application's code here
    cp = request.args.get('cap')
    livro = loadDados()[cp]
    print(livro)
    return render_template('app.html', texto=livro)

@app.route('/')
def index():
    dados = loadDados()
    return render_template('index.html', dados=dados)

if __name__ == '__main__':
    app.run()

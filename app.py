from flask import Flask, render_template, request
import requests
from rotinas import int_to_Roman

app = Flask(__name__)


@app.route('/detalhes/')
def hello_world():  # put application's code here
    cp = request.args.get('cap')
    return render_template('app.html', cp=cp)

@app.route('/')
def index():
    dados = requests.get('https://raw.githubusercontent.com/grovina/assisnet/master/casmurro.txt').text
    indice = {}
    for cap in range(1, 149):
        rom_cap_inicio = int_to_Roman(cap)
        rom_cap_fim = int_to_Roman(cap + 1)
        print(rom_cap_inicio + '>>' + rom_cap_fim)
        if cap == 1:
            capitulo = dados.split('\n' + rom_cap_inicio)[0].split('\n' + rom_cap_fim)[0]
        else:
            capitulo = dados.split('\n' + rom_cap_inicio)[1].split('\n' + rom_cap_fim)[0]
        indice['CAP: ' + rom_cap_inicio + ' >> ' + capitulo.replace('\n', '').replace('\r', '')[0:20].split('.')[0]] = \
            capitulo.replace('\n', '<br>').replace('\r', '')
    return render_template('index.html', dados=indice)

if __name__ == '__main__':
    app.run()

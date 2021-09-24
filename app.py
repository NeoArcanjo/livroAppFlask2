from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    dados = requests.get('https://raw.githubusercontent.com/grovina/assisnet/master/casmurro.txt').text.split('II')[0]
    dados = dados.replace('\n','<br>').replace('\r','')
    return render_template('app.html', dados=dados)


if __name__ == '__main__':
    app.run()

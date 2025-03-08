from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetriz', 'Puzzle', 'Atari')
jogo2 = Jogo('Gold Of War', 'War', 'Ps2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'Ps2')

lista = [jogo1, jogo2, jogo3]


@app.route('/')
def index():

    coluna1_lista1 = 'Jogo'
    coluna2_lista1 = 'Categoria'
    coluna3_lista1 = 'Console'

    return render_template('lista.html', titulo='Início', coluna1=coluna1_lista1, coluna2=coluna2_lista1, coluna3=coluna3_lista1, jogos=lista)

@app.route('/new')
def new():
    return render_template('new.html', titulo='Novo Jogo')

@app.route('/create', methods=['POST',])
def create():

    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)

    lista.append(jogo)

    #return render_template('lista.html', titulo='Jogos autualizados', jogos=lista)
    return redirect('/')


app.run(debug=True)

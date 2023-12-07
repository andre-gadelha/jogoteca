from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def ola():

    coluna1_lista1 = 'Jogo'
    coluna2_lista1 = 'Categoria'
    coluna3_lista1 = 'Console'

    jogo1 = Jogo('Tetriz', 'Puzzle', 'Atari')
    jogo2 = Jogo('Gold Of War', 'War', 'Ps2')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'Ps2')

    itens_lista = [jogo1, jogo2, jogo3]

    return render_template('lista.html', titulo='Início', coluna1=coluna1_lista1, coluna2=coluna2_lista1, coluna3=coluna3_lista1, obj_lista=itens_lista)

app.run()

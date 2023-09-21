from flask import Flask, render_template,request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, World!'

@app.route('/meu-nome')
def meu_nome():
    return 'Meu nome é Filipe!'

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/produtos')
def produtos():
    produtos = [
        ('Produto 1', 100),
        ('Produto 2', 200),
        ('Produto 3', 300),
    ]
    return render_template('produtos.html', produtos=produtos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validar os dados do formulário
        if request.form['nome_usuario'] == 'admin' and request.form['senha'] == '123456':
            return redirect('/')
        else:
            return render_template('login.html', error=True)
    else:
        return render_template('login.html')


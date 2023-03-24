from flask import Flask, request # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

#    http://127.0.0.1:5000/?n1=32&n2=19

@app.route('/') # Cria uma rota
def main():
    print('request:', request)
    n1 = request.args.get('n1')
    n2 = request.args.get('n2')
    print('n1:', n1)
    print('n2:', n2)
    if n1 and n2:
        n1 = float(n1)
        n2 = float(n2)

        media = (n1 + n2) / 2
        return 'A média é: ' + str(media)
    
if __name__ == '__main__':
    app.run(debug=True) # Executa a aplicação

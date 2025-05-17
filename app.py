from flask import Flask, jsonify,render_template
import requests

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Olá, mundo!"), 200


@app.route('/senai', methods=['GET'])
def senai():
    return jsonify(message="Olá, turma python com framework!"), 200


#endpoint - pesquisar endereço atraves do cep, retorna em formato json
@app.route('/pesquisacep/<cep>', methods=['GET'])
def pesquisacep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    return resposta.json()


#endpoint - temperatura
@app.route('/tempo', methods=['GET'])
def temperatura():


    url = f"https://api.weatherapi.com/v1/current.json?key=c4380707dde242f4b78202712252204&q=Sao Paulo&lang=pt"

    resposta=requests.get(url)
    result=resposta.json()

    temperatura = result['current']['temp_c']
    umidade = result['current']['humidity']

    return render_template("pagtempo.html",
    temp=temperatura, umid=umidade)








if __name__ == '__main__':
    app.run(debug=True)
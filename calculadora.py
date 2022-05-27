import os
import math
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('calculadora.html')

@app.route("/calculadora", methods=["POST", "GET"])
def calculo():
    getRequest = request.form.get
    valor1 =  getRequest('v1')
    valor2 =  getRequest('v2')
    operacao = request.form['operacao']

    if valor1 and valor2:
        if operacao == '1':
            return jsonify(float(valor1) + float(valor2))
        elif operacao == '2':
            return jsonify(float(valor1) - float(valor2))
        elif operacao == '3':
            return jsonify(float(valor1) / float(valor2))
        elif operacao == '4':
            return jsonify(float(valor1) * float(valor2))
        elif operacao == '5':
            return jsonify(float(valor1) ** float(valor2))
        
        else:
            return 'error'
    elif valor1 :
        if operacao == '6':
            return jsonify(math.isqrt(int(valor1)))
        elif operacao == '7':
            return jsonify(math.log10(int(valor1)))
        return 'error'

    else:
        return 'Error: Preencha ao menos um valor para realizar o cálculo.'


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
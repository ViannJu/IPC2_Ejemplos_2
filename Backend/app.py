from doctest import register_optionflag
from flask import Flask, request, jsonify

app = Flask(__name__)
registros = []

@app.route('/')
def Hola():
    return "Hola Mundo en flask"

@app.route('/getDatos', methods =['POST'])
def postDatos():
    carnet = request.form['carnet']
    nombre = request.form['nombre']
    estudiante = {
        "carnet": carnet,
        "nombre": nombre
    }
    registros.append(estudiante)
    retorno = {
        "msg": "Insertado correctamente"
    }
    print(registros)

    return jsonify(retorno), 200



@app.route("/visualizar", methods=['GET'])
def visualizar():
    return jsonify(registros), 200






if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True, port = 8080)
import random
from flask import Flask, jsonify
app = Flask(__name__) #iniciar la ruta básica del flask


#diccionario de datos
listaEstudiates = []
listaEstudiates.append({"carnet": "201800001", "nombre": "Estudiante Viany"})
listaEstudiates.append({"carnet": "201800002", "nombre": "Estudiante 2"})
listaEstudiates.append({"carnet": "201800003", "nombre": "Estudiante 3"})
listaEstudiates.append({"carnet": "201800004", "nombre": "Estudiante 4"})
listaEstudiates.append({"carnet": "201800005", "nombre": "Estudiante 5"})
listaEstudiates.append({"carnet": "201800006", "nombre": "Estudiante 6"})
listaEstudiates.append({"carnet": "201800007", "nombre": "Estudiante 7"})
listaEstudiates.append({"carnet": "201800008", "nombre": "Estudiante 8"})
listaEstudiates.append({"carnet": "201800009", "nombre": "Estudiante 9"})
listaEstudiates.append({"carnet": "201800010", "nombre": "Estudiante 10"})
listaEstudiates.append({"carnet": "201800011", "nombre": "Paola"})

@app.route('/estudiante', methods=['GET'])
def getEstudiante():
    estudiante = random.choice(listaEstudiates)
    return jsonify(estudiante)

if __name__ == '__main__':
    app.run(debug=True)
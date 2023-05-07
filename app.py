from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.personas_blueprint import personas_blueprint
from backend.blueprints.alumnos_blueprint import alumnos_blueprint
from backend.blueprints.profesores_blueprint import profesores_blueprint
from backend.blueprints.asignaturas_blueprint import asignaturas_blueprint
from backend.blueprints.salones_blueprint import salones_blueprint
from backend.blueprints.administradores_blueprint import administradores_blueprint
from backend.blueprints.horarios_blueprint import horarios_blueprint
from backend.blueprints.justificaciones_blueprint import justificaciones_blueprint
from backend.blueprints.cursos_blueprint import cursos_blueprint
from backend.blueprints.dictados_blueprint import dictados_blueprint

app = Flask(__name__)

app.register_blueprint(personas_blueprint)
app.register_blueprint(alumnos_blueprint)
app.register_blueprint(profesores_blueprint)
app.register_blueprint(asignaturas_blueprint)
app.register_blueprint(salones_blueprint)
app.register_blueprint(administradores_blueprint)
app.register_blueprint(horarios_blueprint)
app.register_blueprint(justificaciones_blueprint)
app.register_blueprint(cursos_blueprint)
app.register_blueprint(dictados_blueprint)

cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
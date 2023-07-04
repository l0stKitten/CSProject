from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_jwt_extended import jwt_required
from flask_cors import CORS, cross_origin 

from backend.models.post_alumnos_model import AlumnoModel
model = AlumnoModel()


alumnos_blueprint = Blueprint('alumnos_blueprint', __name__)

@alumnos_blueprint.route('/alumno', methods=['PUT'])
@jwt_required()
@cross_origin()
def create_alumno():
    content = model.create_alumno(request.json['dni'])    
    return jsonify(content)

@alumnos_blueprint.route('/alumno', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete_alumno():
    return jsonify(model.delete_alumno(request.json['dni']))

@alumnos_blueprint.route('/alumno', methods=['POST'])
@jwt_required()
@cross_origin()
def get_alumno():
    return jsonify(model.get_alumno(request.json['dni']))

@alumnos_blueprint.route('/alumnos', methods=['POST'])
@jwt_required()
@cross_origin()
def get_alumnos():
    return jsonify(model.get_alumnos())

@alumnos_blueprint.route('/alumnoscurso', methods=['POST'])
@jwt_required()
@cross_origin()
def get_alumnos_curso():
    return jsonify(model.get_alumnos_curso(request.json['codigo'], request.json['fecha']))
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 
from flask_jwt_extended import jwt_required

from backend.models.post_cursos_model import CursoModel
model = CursoModel()


cursos_blueprint = Blueprint('cursos_blueprint', __name__)


@cursos_blueprint.route('/curso', methods=['PUT'])
@jwt_required()
@cross_origin()
def create_curso():
    content = model.create_curso(request.json['asignatura'], request.json['profesor'], request.json['horario'])    
    return jsonify(content)

@cursos_blueprint.route('/curso', methods=['PATCH'])
@jwt_required()
@cross_origin()
def update_curso():
    content = model.update_curso(request.json['codigo'], request.json['asignatura'], request.json['profesor'], request.json['horario'])    
    return jsonify(content)

@cursos_blueprint.route('/curso', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete_curso():
    return jsonify(model.delete_curso(request.json['codigo']))

@cursos_blueprint.route('/curso', methods=['POST'])
@jwt_required()
@cross_origin()
def get_curso():
    return json.dumps(model.get_curso(request.json['codigo']), default=str)

@cursos_blueprint.route('/cursos', methods=['POST'])
@jwt_required()
@cross_origin()
def get_cursos():
    return json.dumps(model.get_cursos(), default=str)

@cursos_blueprint.route('/cursosuser', methods=['POST'])
@jwt_required()
@cross_origin()
def get_cursos_user():
    return json.dumps(model.get_cursos_usuario(request.json['dni']), default=str)

@cursos_blueprint.route('/cursosprof', methods=['POST'])
@jwt_required()
@cross_origin()
def get_cursos_prof():
    return json.dumps(model.get_cursos_prof(request.json['dni']), default=str)
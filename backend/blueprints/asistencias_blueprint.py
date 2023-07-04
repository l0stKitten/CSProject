from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 
from flask_jwt_extended import jwt_required

from backend.models.post_asistencias_model import AsistenciaModel
model = AsistenciaModel()


asistencias_blueprint = Blueprint('asistencias_blueprint', __name__)

@asistencias_blueprint.route('/asistencia', methods=['PUT'])
@jwt_required()
@cross_origin()
def create_asistencia():
    content = model.create_asistencia(request.json['path'], request.json['fecha_asistencia'], request.json['matricula'], request.json['dni'])    
    return jsonify(content)

@asistencias_blueprint.route('/asistencia', methods=['PATCH'])
@jwt_required()
@cross_origin()
def update_asistencia():
    content = model.update_asistencia(request.json['codigo'], request.json['estado'], request.json['fecha_asistencia'], request.json['matricula'])    
    return jsonify(content)

@asistencias_blueprint.route('/asistencia', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete_asistencia():
    return jsonify(model.delete_asistencia(request.json['codigo']))

@asistencias_blueprint.route('/asistencia', methods=['POST'])
@jwt_required()
@cross_origin()
def get_asistencia():
    return jsonify(model.get_asistencia(request.json['codigo']))

@asistencias_blueprint.route('/asistencias', methods=['POST'])
@jwt_required()
@cross_origin()
def get_asistencias():
    return jsonify(model.get_asistencias())
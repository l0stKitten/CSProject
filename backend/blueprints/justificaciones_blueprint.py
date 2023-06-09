from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_justificaciones_model import JustificacionModel
model = JustificacionModel()


justificaciones_blueprint = Blueprint('justificaciones_blueprint', __name__)

@justificaciones_blueprint.route('/justificacion', methods=['PUT'])
@jwt_required()
@cross_origin()
def create_justificacion():
    content = model.create_justificacion(request.json['asistencia'], request.json['titulo'], request.json['descripcion'])    
    return jsonify(content)

@justificaciones_blueprint.route('/justificacion', methods=['PATCH'])
@jwt_required()
@cross_origin()
def update_justificacion():
    content = model.update_justificacion(request.json['codigo'], request.json['asistencia'], request.json['titulo'], request.json['descripcion'])    
    return jsonify(content)

@justificaciones_blueprint.route('/justificacion', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete_justificacion():
    return jsonify(model.delete_justificacion(request.json['codigo']))

@justificaciones_blueprint.route('/justificacion', methods=['POST'])
@jwt_required()
@cross_origin()
def get_justificacion():
    return jsonify(model.get_justificacion(request.json['codigo']))

@justificaciones_blueprint.route('/justificaciones', methods=['POST'])
@jwt_required()
@cross_origin()
def get_justificaciones():
    return jsonify(model.get_justificaciones())
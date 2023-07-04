from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_participaciones_model import ParticipacionModel
model = ParticipacionModel()


participaciones_blueprint = Blueprint('participaciones_blueprint', __name__)

@participaciones_blueprint.route('/participacion', methods=['PUT'])
@jwt_required()
@cross_origin()
def create_participacion():
    content = model.create_participacion(request.json['asistencia'], request.json['cantidad'])    
    return jsonify(content)

@participaciones_blueprint.route('/participacion', methods=['PATCH'])
@jwt_required()
@cross_origin()
def update_participacion():
    content = model.update_participacion(request.json['asistencia'], request.json['cantidad'])    
    return jsonify(content)

@participaciones_blueprint.route('/participacion', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete_participacion():
    return jsonify(model.delete_participacion(request.json['asistencia']))

@participaciones_blueprint.route('/participacion', methods=['POST'])
@jwt_required()
@cross_origin()
def get_participacion():
    return jsonify(model.get_participacion(request.json['asistencia']))

@participaciones_blueprint.route('/participaciones', methods=['POST'])
@jwt_required()
@cross_origin()
def get_participaciones():
    return jsonify(model.get_participaciones())
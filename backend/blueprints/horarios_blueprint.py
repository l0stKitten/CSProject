from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_horarios_model import HorarioModel
model = HorarioModel()


horarios_blueprint = Blueprint('horarios_blueprint', __name__)


@horarios_blueprint.route('/horario', methods=['PUT'])
@cross_origin()
def create_horario():
    content = model.create_horario(request.json['hora_inicio'], request.json['hora_fin'], request.json['dia'])    
    return jsonify(content)

@horarios_blueprint.route('/horario', methods=['PATCH'])
@cross_origin()
def update_horario():
    content = model.update_horario(request.json['codigo'], request.json['hora_inicio'], request.json['hora_fin'], request.json['dia'])    
    return jsonify(content)

@horarios_blueprint.route('/horario', methods=['DELETE'])
@cross_origin()
def delete_horario():
    return jsonify(model.delete_horario(request.json['codigo']))

@horarios_blueprint.route('/horario', methods=['POST'])
@cross_origin()
def get_horario():
    return jsonify(model.get_horario(request.json['codigo']))

@horarios_blueprint.route('/horarios', methods=['POST'])
@cross_origin()
def get_horarios():
    return jsonify(model.get_horarios())
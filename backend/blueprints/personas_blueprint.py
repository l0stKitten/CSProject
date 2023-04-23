from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_personas_model import PersonaModel
model = PersonaModel()


personas_blueprint = Blueprint('personas_blueprint', __name__)


@personas_blueprint.route('/persona', methods=['PUT'])
@cross_origin()
def create_persona():
    content = model.create_persona(request.json['dni'], request.json['nombres'], request.json['apellido_paterno'], 
                                request.json['apellido_materno'], request.json['fecha_nacimiento'], request.json['correo_institucional'],
                                request.json['password'])    
    return jsonify(content)

@personas_blueprint.route('/persona', methods=['PATCH'])
@cross_origin()
def update_persona():
    content = model.update_persona(request.json['dni'], request.json['nombres'], request.json['apellido_paterno'], 
                                request.json['apellido_materno'], request.json['fecha_nacimiento'], request.json['correo_institucional'],
                                request.json['password'])    
    return jsonify(content)

@personas_blueprint.route('/persona', methods=['DELETE'])
@cross_origin()
def delete_persona():
    return jsonify(model.delete_persona(request.json['dni']))

@personas_blueprint.route('/persona', methods=['POST'])
@cross_origin()
def get_persona():
    return jsonify(model.get_persona(request.json['dni']))

@personas_blueprint.route('/personas', methods=['POST'])
@cross_origin()
def get_personas():
    return jsonify(model.get_personas())
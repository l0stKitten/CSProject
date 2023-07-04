from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_matriculas_model import MatriculaModel
model = MatriculaModel()


matriculas_blueprint = Blueprint('matriculas_blueprint', __name__)

@matriculas_blueprint.route('/matricula', methods=['PUT'])
@jwt_required()
@cross_origin()
def create_matricula():
    content = model.create_matricula(request.json['alumno'], request.json['curso'], request.json['estado'])    
    return jsonify(content)

@matriculas_blueprint.route('/matricula', methods=['PATCH'])
@jwt_required()
@cross_origin()
def update_matricula():
    content = model.update_matricula(request.json['codigo'], request.json['alumno'], request.json['curso'], request.json['estado'])    
    return jsonify(content)

@matriculas_blueprint.route('/matricula', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete_matricula():
    return jsonify(model.delete_matricula(request.json['codigo']))

@matriculas_blueprint.route('/matricula', methods=['POST'])
@jwt_required()
@cross_origin()
def get_matricula():
    return jsonify(model.get_matricula(request.json['codigo']))

@matriculas_blueprint.route('/matriculas', methods=['POST'])
@jwt_required()
@cross_origin()
def get_matriculas():
    return jsonify(model.get_matriculas())
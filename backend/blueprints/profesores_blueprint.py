from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_profesores_model import ProfesorModel
model = ProfesorModel()


profesores_blueprint = Blueprint('profesores_blueprint', __name__)

@profesores_blueprint.route('/profesor', methods=['PUT'])
@jwt_required()
@cross_origin()
def create_profesor():
    content = model.create_profesor(request.json['dni'], request.json['especialidad'])    
    return jsonify(content)

@profesores_blueprint.route('/profesor', methods=['PATCH'])
@jwt_required()
@cross_origin()
def update_profesor():
    content = model.update_profesor(request.json['dni'], request.json['especialidad'])    
    return jsonify(content)

@profesores_blueprint.route('/profesor', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete_profesor():
    return jsonify(model.delete_profesor(request.json['dni']))

@profesores_blueprint.route('/profesor', methods=['POST'])
@jwt_required()
@cross_origin()
def get_profesor():
    return jsonify(model.get_profesor(request.json['dni']))

@profesores_blueprint.route('/profesores', methods=['POST'])
@jwt_required()
@cross_origin()
def get_profesores():
    return jsonify(model.get_profesores())
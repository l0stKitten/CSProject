from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_administradores_model import AdminModel
model = AdminModel()


administradores_blueprint = Blueprint('administradores_blueprint', __name__)

@administradores_blueprint.route('/administrador', methods=['PUT'])
@jwt_required()
@cross_origin()
def create_administrador():
    content = model.create_administrador(request.json['dni'], request.json['cargo'])    
    return jsonify(content)

@administradores_blueprint.route('/administrador', methods=['PATCH'])
@jwt_required()
@cross_origin()
def update_administrador():
    content = model.update_administrador(request.json['dni'], request.json['cargo'])    
    return jsonify(content)

@administradores_blueprint.route('/administrador', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete_administrador():
    return jsonify(model.delete_administrador(request.json['dni']))

@administradores_blueprint.route('/administrador', methods=['POST'])
@jwt_required()
@cross_origin()
def get_administrador():
    return jsonify(model.get_administrador(request.json['dni']))

@administradores_blueprint.route('/administradores', methods=['POST'])
@jwt_required()
@cross_origin()
def get_administradores():
    return jsonify(model.get_administradores())
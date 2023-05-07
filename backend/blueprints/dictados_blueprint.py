from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_dictados_model import DictadoModel
model = DictadoModel()


dictados_blueprint = Blueprint('dictados_blueprint', __name__)


@dictados_blueprint.route('/dictado', methods=['PUT'])
@cross_origin()
def create_dictado():
    content = model.create_dictado(request.json['curso'], request.json['salon'], request.json['tema'])    
    return jsonify(content)

@dictados_blueprint.route('/dictado', methods=['PATCH'])
@cross_origin()
def update_dictado():
    content = model.update_dictado(request.json['codigo'], request.json['curso'], request.json['salon'], request.json['tema'])    
    return jsonify(content)

@dictados_blueprint.route('/dictado', methods=['DELETE'])
@cross_origin()
def delete_dictado():
    return jsonify(model.delete_dictado(request.json['codigo']))

@dictados_blueprint.route('/dictado', methods=['POST'])
@cross_origin()
def get_dictado():
    return jsonify(model.get_dictado(request.json['codigo']))

@dictados_blueprint.route('/dictados', methods=['POST'])
@cross_origin()
def get_dictados():
    return jsonify(model.get_dictados())
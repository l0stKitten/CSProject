from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_authentication_model import AuthModel
model = AuthModel()


authentication_blueprint = Blueprint('authentication_blueprint', __name__)


@authentication_blueprint.route('/login', methods=['POST'])
@cross_origin()
def login_get_persona():
    return jsonify(model.login_get_persona(request.json['dni'], request.json['password']))

@authentication_blueprint.route('/decodetoken', methods=['POST'])
@cross_origin()
def dec_token():
    return jsonify(model.dec_token(request.json['token']))
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.formulario_controller import FormularioController

formulario_bp = Blueprint('formularios', __name__)

@formulario_bp.route('/', methods=['POST'])
@jwt_required()
def create_formulario():
    user_id = get_jwt_identity()
    return jsonify(FormularioController.create_formulario(user_id,request.get_json()))

@formulario_bp.route('/ge', methods=['GET'])
@jwt_required()
def listar_user():
    user_id = get_jwt_identity()
    return jsonify(FormularioController.listar_user(user_id,request.get_json()))

@formulario_bp.route('/pu/<int:user_id>', methods=['PUT'])
@jwt_required()
def put_user():
    user_id = get_jwt_identity()
    return jsonify(FormularioController.put_user(user_id,request.get_json()))


@formulario_bp.route('/de/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user():
    user_id = get_jwt_identity()
    return jsonify(FormularioController.delete_user(user_id,request.get_json()))
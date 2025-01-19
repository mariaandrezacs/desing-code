from flask import Blueprint, jsonify, request

calc_rout_bp = Blueprint("calc_routes", __name__)

@calc_rout_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    print(request.json)     # caputura o body da requisição
    return jsonify({"sucess": True})
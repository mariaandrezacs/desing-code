from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calc_rout_bp = Blueprint("calc_routes", __name__)

@calc_rout_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    # print(request.json)     # caputura o body da requisição
    calc = Calculator1()
    calc.calculate(request)
    return jsonify({"sucess": True})
from flask import Blueprint, jsonify, request
from ..factories.calculator1_factory import calculator1_factory
from ..factories.calculator2_factory import calculator2_factory

calc_rout_bp = Blueprint("calc_routes", __name__)

@calc_rout_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    # print(request.json)     # caputura o body da requisição
    calc = calculator1_factory()
    response = calc.calculate(request)
    return jsonify(response)

@calc_rout_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    calc = calculator2_factory()
    response = calc.calculate(request)
    return jsonify(response)
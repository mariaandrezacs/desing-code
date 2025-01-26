from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1
from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

calc_rout_bp = Blueprint("calc_routes", __name__)

@calc_rout_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    # print(request.json)     # caputura o body da requisição
    calc = Calculator1()
    response = calc.calculate(request)
    return jsonify(response)

@calc_rout_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    numpy_handler = NumpyHandler()
    calc = Calculator2(numpy_handler)
    response = calc.calculate(request)
    return jsonify(response)
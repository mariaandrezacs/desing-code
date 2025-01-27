from typing import Dict, List
from flask import request as FlaskRequest
from ..drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from ..errors.http_unprocessable_entity import HttpUnprocessableEntity
from ..errors.http_bad_request import HttpBadRequestError


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__varify_result(variance, multiplication)
        formated_response = self.__format_response(variance)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntity("body mal formatado!")

        input_date = body["numbers"]
        return input_date

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication

    def __varify_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError(
                "Falha no process: Variância menor que multiplicação"
            )

    def __format_response(self, variance: float) -> Dict:
        return {"data": {"Calculator": 3, "value": variance, "Sucess": True}}

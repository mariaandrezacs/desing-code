from typing import Dict
from .calculator_2 import Calculator2


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
        pass


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    calculate_2 = Calculator2()
    formated_response = calculate_2.calculate(mock_request)
    print()
    print(formated_response)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.08}}

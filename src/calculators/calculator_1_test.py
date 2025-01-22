from typing import Dict
from .calculator_1 import Calculator1


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
        pass


def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)
    print()
    print(response)

    # 1 - formato da resposta / tipagem
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # 2 - Assertividade da reposta
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

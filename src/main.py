from typing import Union

class Bikes():
    engine = 49
    type = 'scooter'
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model



class Calc():
    @staticmethod
    def divine(a,b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Params are not invalid")
        if b == 0:
            raise ZeroDivisionError("Do not divide by zero")
        return a / b

    @staticmethod
    def plus(a,b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Params are not valid")
        return a + b

import pytest
from src.main import Bikes, Calc
from contextlib import nullcontext as does_not_raise


def test_start():
    x = Bikes.engine
    y = 48
    assert x != y , "Nums are not equal"

class TestCalc():
    @pytest.mark.parametrize("x,y, expect", [(8,0, pytest.raises(ZeroDivisionError)),(6,1, does_not_raise())])
    def test_divine(self, x, y, expect):
        with expect:
            result = x / y
            assert result == Calc.divine(x, y), "Calc is not working"


    @pytest.mark.parametrize("x, y, result, expectation", [(1, 1, 2, does_not_raise()), (2, 2, 4, does_not_raise()),\
                             (3, '3', 33, pytest.raises(ValueError))])
    def test_plus(self, x, y,result, expectation):
        with expectation:
            assert result == Calc.plus(x, y), "Plus feature is broken"

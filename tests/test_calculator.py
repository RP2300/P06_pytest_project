import pytest
from Calculator.calculator import Calculator
class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
        
    def test_sub(self):
        #arrange
        a = 3700
        b = 700
        cal = Calculator()
        
        #act 
        result = cal.subtract(a,b)
        
        #assert
        expected = 3000
        assert result == expected
        
    def test_multi(self):
        #arrange
        a = 5
        b = 10
        cal = Calculator()
        
        #act
        result = cal.multiply(a,b)
        
        #assert
        expected = 50
        assert result == expected
        
    def test_Divide(self):
        #arrange
        a = 100
        b = 5
        cal = Calculator()
        
        #act
        result = cal.divide(a,b)
        
        #assert
        expected = 20
        assert result == expected
        
    def test_Divide1(self):
        #arrange
        a = 100
        b = 0
        cal = Calculator()
        
        #act and assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)
        

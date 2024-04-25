from src.calculator import Calculator


class Test_Calculator:


    def test_media(self):
        result = Calculator.media(9, 3)
        assert result == 6


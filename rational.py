from fractions import Fraction

class Rational:
    def __init__(self, numerator, denominator=1):
        self.value = Fraction(numerator, denominator)

    def __repr__(self):
        if self.value.denominator == 1:
            return f"{self.value.numerator}"
        return f"{self.value.numerator}/{self.value.denominator}"
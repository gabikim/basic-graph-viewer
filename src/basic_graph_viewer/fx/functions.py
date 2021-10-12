#!/usr/bin/env python

"""
Custom functions
"""

import numpy as np

from .baseclass import Function


class SineWave(Function):
    "Sine wave custom function"
    A = 1
    B = 1
    x_range = (-10, 10)

    @property
    def description_A(self) -> str:
        "Returns description of A"
        return "Amplitude. -inf<A<inf"

    @property
    def description_B(self) -> str:
        "Returns description of B"
        return "Period. -inf<B<inf"

    @property
    def description_fx(self) -> str:
        "Returns description of function f(x)"
        return "sin function, f(x)=Asin(Bx)"

    def gen_y_point(self, x_val):
        "Returns result of f(x)=Asin(Bx)"
        y = self.A * np.sin(self.B * x_val)
        return y


class Power(Function):
    "Power custom function"
    A = 1
    B = 2
    x_range = (-25, 25)

    @property
    def description_A(self) -> str:
        "Returns description of A"
        return "Coefficient. -inf<A<inf"

    @property
    def description_B(self) -> str:
        "Returns description of B"
        return "Degree. -inf<B<inf"

    @property
    def description_fx(self) -> str:
        "Returns description of function f(x)"
        return "power function, f(x)=Ax^B"

    def gen_y_point(self, x_val):
        "Returns result of f(x)=Ax^B"
        y = self.A * (x_val ** self.B)
        return y


class SawTooth(Function):
    "Sawtooth function."
    A = 1
    B = 0
    x_range = (-25, 25)

    @property
    def description_A(self) -> str:
        "Returns description of A"
        return "Amplitude. -inf<A<inf"

    @property
    def description_B(self) -> str:
        "Returns description of B"
        return "Vertical pos. -inf<B<inf"

    @property
    def description_fx(self) -> str:
        "Returns description of function f(x)"
        return "Sawtooth: asymmetric triangle wave function"

    def gen_y_point(self, x_val):
        "Returns result of sawtooth function"
        period = 4
        remainder = x_val % period
        if 0 <= remainder <= 1:
            y = self.B
        elif 1 < remainder <= 2:
            y = self.A * (remainder - 1) + self.B
        elif 2 < remainder < 4:
            y = -(self.A / 2) * (remainder - 2) + self.A + self.B

        return y

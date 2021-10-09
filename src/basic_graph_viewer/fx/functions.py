#!/usr/bin/env python

"""
Custom functions
"""
from .baseclass import Function


class SineWave(Function):
    A = 1
    B = 1
    x_range = (-10, 10)

    @property
    def description_A(self) -> str:
        "Returns description of A"
        return "Amplitude"

    @property
    def description_B(self) -> str:
        "Returns description of B"
        return "Period"

    @property
    def description_fx(self) -> str:
        "Returns description of function f(x)"
        return "sin function, f(x)=Asin(Bx)"

#!/usr/bin/env python

"""
Base class for f(x).
"""

import traceback
import typing

import numpy as np


class Function:
    """
    Defines standard methods and properties that all functions should have.
    """

    A: float = 0  # Default user adjustable param
    B: float = 0  # Default user adjustable param
    x_lower: float = 0  # Default x lower limit
    x_upper: float = 10  # Default x upper limit
    x_points: int = 10000  # Granularity --num of points to plot

    @property
    def description_A(self) -> str:
        "Returns description of A"
        raise NotImplementedError

    @property
    def description_B(self) -> str:
        "Returns description of B"
        raise NotImplementedError

    @property
    def description_fx(self) -> str:
        "Returns description of function f(x)"
        raise NotImplementedError

    def gen_y_point(self, x_val) -> typing.Optional[float]:
        """Generate y value given an x value.
        Allows for easier implementation without dealing with lists or vectors.
        """
        raise NotImplementedError

    def check_valid_A(self) -> bool:
        "Checks if A is valid. Default to True"
        return True

    def check_valid_B(self) -> bool:
        "Checks if B is valid. Default to True"
        return True

    def _gen_y_point(self, x_val) -> typing.Optional[float]:
        "Catches errors and returns NaN"
        try:
            return self.gen_y_point(x_val)
        except Exception:
            print(traceback.format_exc())
            return np.NaN

    @property
    def y_vect(self):
        "Returns y-vector"
        y = np.array([self._gen_y_point(x) for x in self.x_vect])
        return y

    @property
    def x_vect(self):
        "Returns x-vector within specified range"
        step_size = (self.x_upper - self.x_lower) / self.x_points
        return np.arange(self.x_lower, self.x_upper, step_size)

    def update_A(self, new_value: float) -> bool:
        "Updates A. Returns True if successful, False otherwise."
        if isinstance(new_value, float) and self.check_valid_A():
            self.A = new_value
            return True
        return False

    def update_B(self, new_value: float) -> bool:
        "Updates B. Returns True if successful, False otherwise."
        if isinstance(new_value, float) and self.check_valid_B():
            self.B = new_value
            return True
        return False

    def update_x_lower(self, new_value):
        "Updates x lower limit. Returns True if successful, False otherwise."
        if isinstance(new_value, float) and new_value < self.x_upper:
            self.x_lower = new_value
            return True
        return False

    def update_x_upper(self, new_value):
        "Updates x upper limit. Returns True if successful, False otherwise."
        if isinstance(new_value, float) and new_value > self.x_lower:
            self.x_upper = new_value
            return True
        return False

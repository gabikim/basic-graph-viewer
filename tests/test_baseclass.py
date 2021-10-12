#!/usr/bin/env python

"""
Tests the function baseclass
"""

import numpy as np
import pytest

from basic_graph_viewer.fx import Function


class TestClass(Function):
    def gen_y_point(self, x_val):
        return 1 / x_val


def test_default_values():
    "Tests default values A, B, x_range and x_points"
    func = Function()
    assert func.A == 0
    assert func.B == 0
    assert func.x_lower == 0
    assert func.x_upper == 10
    assert func.x_points == 1000


def test_description_A_not_implemented():
    "Tests that NotImplementedError is raised for key property A."
    func = Function()
    with pytest.raises(NotImplementedError):
        func.description_A


def test_description_B_not_implemented():
    "Tests that NotImplementedError is raised for key property B."
    func = Function()
    with pytest.raises(NotImplementedError):
        func.description_B


def test_description_fx_not_implemented():
    "Tests that NotImplementedError is raised for key property description fx."
    func = Function()
    with pytest.raises(NotImplementedError):
        func.description_fx


def test_gen_y_point_not_implemented():
    "Tests that NotImplementedError is raised for gen_y_point."
    func = Function()
    with pytest.raises(NotImplementedError):
        func.gen_y_point(1)


def test_valid_A_B():
    "Tests valid A and B defaults"
    func = Function()
    assert func.check_valid_A()
    assert func.check_valid_B()


def test_gen_y_point():
    "Tests function with asymptote at 0 gives inf, errored, and happy path."
    func = TestClass()
    # Happy
    y = func._gen_y_point(1)
    assert y == 1
    # Asymptote
    y = func._gen_y_point(func.x_vect[0])
    assert np.isinf(y)
    # Not implemented
    func = Function()
    y = func._gen_y_point(1)
    assert y is np.nan


def test_x_vector():
    "Tests generating the x-vector"
    func = Function()
    x_vect = func.x_vect
    assert len(x_vect) == func.x_points
    assert x_vect[0] == func.x_lower
    assert x_vect[-1] <= func.x_upper


def test_y_vect():
    "Tests the y-vector generation"
    func = TestClass()
    y_vect = func.y_vect
    assert len(y_vect) == func.x_points

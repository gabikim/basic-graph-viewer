#!/usr/bin/env python

"""
Tests for the custom functions
"""
import numpy as np

from basic_graph_viewer import fx, tools


def test_all_descriptions():
    "Tests that all description properties are defined."
    fcns = tools.get_subclasses(fx.Function)
    for name, fcn in fcns.items():
        if name == "TestClass":
            continue
        c = fcn()
        assert isinstance(c.description_A, str)
        assert isinstance(c.description_B, str)
        assert isinstance(c.description_fx, str)


def test_sine_y():
    "Tests generating the y value for sine."
    sine = fx.SineWave()
    assert sine.gen_y_point(0) == 0
    assert sine.gen_y_point(np.pi / 2) == 1
    sine.update_A(5.0)
    assert sine.gen_y_point(np.pi / 2) == 5
    sine.update_B(1 / 2)
    assert sine.gen_y_point(np.pi) == 5


def test_power_y():
    "Tests generating the y value for power"
    power = fx.Power()
    assert power.gen_y_point(0) == 0
    assert power.gen_y_point(2) == 4
    power.update_A(2.0)
    assert power.gen_y_point(2) == 8
    power.update_B(3.0)
    assert power.gen_y_point(2) == 16


def test_sawtooth():
    "Tests generating values for sawtooth wave"
    sawtooth = fx.SawTooth()
    assert sawtooth.gen_y_point(0) == 0
    assert sawtooth.gen_y_point(0.5) == 0
    assert sawtooth.gen_y_point(1.5) == 0.5
    assert sawtooth.gen_y_point(2) == 1
    assert sawtooth.gen_y_point(3) == 0.5
    assert sawtooth.gen_y_point(4) == 0
    sawtooth.update_A(5.0)
    sawtooth.update_B(6.0)
    assert sawtooth.gen_y_point(0) == 6
    assert sawtooth.gen_y_point(0.5) == 6
    assert sawtooth.gen_y_point(1.5) == 8.5
    assert sawtooth.gen_y_point(2) == 11
    assert sawtooth.gen_y_point(3) == 8.5
    assert sawtooth.gen_y_point(4) == 6

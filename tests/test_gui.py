#!/usr/bin/env python

"""
Tests the gui
"""
from basic_graph_viewer import gui

def test_init(mocker):
    "Tests initializing gui"
    create_label_mock = mocker.patch.object(gui.GUI, "create_label")
    create_widget_set = mocker.patch.object(gui.GUI, "create_widget_set")
    create_dropdown = mocker.patch.object(gui.GUI, "create_dropdown")
    dropdown = mocker.Mock()
    create_dropdown.return_value = dropdown
    dropdown.get.return_value = "SineWave"
    update_function =mocker.patch.object(gui.GUI, "update_function")
    create_widget_set.return_value = (None, None)
    mocked_gui = gui.GUI()
    create_label_mock.assert_called_once()
    create_dropdown.assert_called_once()
    update_function.assert_called_once()
    assert len(create_widget_set.call_args_list) == 4
    assert mocked_gui.canvas
    assert mocked_gui.ax

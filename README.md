# basic-graph-viewer
Allows users to plot functions f(x) with two user-adjustable parameters A and B. Note this program requires >= python 3.7 which should include the tkinter library which is used for the GUI.

## Installation:
`pip3 install -U .`

## To run the graph viewer:
`python3 -m basic_graph_viewer`

## Instructions
1. Choose a function from the blue dropdown menu
2. Adjust parameters A, B, x lower, x upper by entering the value into the box and pressing the enter key or pressing the button to the right.

## Dev Tools
### Install:
`pip3 install -r dev.txt`

### Test + coverage report:
`python3 -m pytest`

### Linting:
`python3 -m pylint ./src`

### Format:
`python3 -m black .`

### mypy:
`python3 -m mypy .`

### isort:
`python3 -m isort .`

## Creating new Functions:
In `src/basic_graph_viewer/fx/functions.py`, add a class that inherits from `Function`. Implement the following methods:
- `description_A`: returns a string describing A
- `description_B`: returns a string describing B
- `description_fx`: returns a string describing f(x)
- `gen_y_point`: param is an x value, returns the specified y value. Useful for piece-wise functions.

To implement time-variant systems, or to simplify, override the property `y_vect` and do not implement `gen_y_point`. 
See `src/basic_graph_viewer/fx/baseclass` for the entire `Function` baseclass.

### TODO
- Aliasing in periodic functions if x range is too big or frequency too high. Should update the `update_x_lower` and `update_x_upper` to also update `x_points`, ie. the number of samples or sample frequency.
- Make an example `Function` class of how to override the property `y_vect`.
- Add more tests in `tests/test_gui.py` to test gui more robustly.

#!/usr/bin/env python

"""
GUI class for the basic graph viewer
"""

import tkinter as tk
from tkinter import messagebox

import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from basic_graph_viewer import fx, tools


class GUI(tk.Frame):
    "GUI class for plots"

    def __init__(self, master=None):
        super().__init__(master)
        self.functions = tools.get_subclasses(fx.Function)
        self.master = master
        self.grid()
        self.create_dropdown()
        self.curr_function = self.functions[self.dropdown_var.get()]()
        self.function_label = self.create_label(self.curr_function, 0, 0)
        self.A_var, self.A_label = self.create_widget_set(
            tools.is_float,
            self.update_A,
            self.curr_function.A,
            "A: " + self.curr_function.description_A,
            1,
        )
        self.B_var, self.B_label = self.create_widget_set(
            tools.is_float,
            self.update_B,
            self.curr_function.B,
            "B: " + self.curr_function.description_B,
            2,
        )
        self.xlow_var, _ = self.create_widget_set(
            tools.is_float,
            self.update_x_low,
            self.curr_function.x_lower,
            "x lower limit",
            3,
        )
        self.xup_var, _ = self.create_widget_set(
            tools.is_float,
            self.update_x_up,
            self.curr_function.x_upper,
            "x upper limit",
            4,
        )

        fig = plt.figure.Figure(figsize=(8, 8))
        self.ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.get_tk_widget().grid(row=0, column=4, rowspan=5)
        self.canvas.draw()

        self.update_function(self.dropdown_var.get())

    def create_widget_set(
        self, validate_cmd, callback, default: float, label_text: str, row: int
    ):
        """Creates a label, entry, and button set.
        Parameters
        validate_cmd: function that validates Entry input
        callback: callback for
        default: default entry value
        label_text: label description
        row: row to put in frame

        Returns
        var: entry variable
        label: label object
        """
        label = self.create_label(label_text, 0, row)
        var = self.create_entry(default, validate_cmd, callback, 1, row)
        self.create_button(callback, "ENTER", 2, row)
        return var, label

    def create_dropdown(self):
        "Creates the functions option menu"
        self.dropdown_var = tk.StringVar(self.master)
        self.dropdown_var.set(list(self.functions.keys())[0])
        menu = tk.OptionMenu(
            self.master,
            self.dropdown_var,
            *list(self.functions.keys()),
            command=self.update_function
        )
        menu.grid(column=1, row=0)
        menu.config(bg="blue")

    def create_label(self, text: str, col: int, row: int):
        "Creates a label. Returns label widget."
        label = tk.Label(self.master, text=text)
        label.grid(column=col, row=row)
        return label

    def create_entry(self, default, validate_cmd, callback, col: int, row: int):
        "Creates entry widget. Returns variable."
        entry_var = tk.StringVar(self.master)
        entry_var.set(default)
        vcmd = self.register(validate_cmd)
        entry = tk.Entry(
            self.master,
            textvariable=entry_var,
            validate="all",
            validatecommand=(vcmd, "%P"),
        )
        entry.bind("<Return>", callback)
        entry.grid(column=col, row=row)
        return entry_var

    def create_button(self, callback, text: str, col: int, row: int):
        "Creates a button"
        button = tk.Button(self.master, text=text, command=callback, bg="blue")
        button.grid(column=col, row=row)

    def update_A(self):
        "Validates and updates A. Displays error message if incorrect."
        if self.curr_function.update_A(tools.str_to_float(self.A_var.get())):
            self.update_plot()
        else:
            messagebox.showinfo(
                message="Error! Invalid A. Please enter new value.\n"
                + self.curr_function.description_A
            )
            self.A_var.set(self.curr_function.A)

    def update_B(self):
        "Validates and updates B. Displays error message if incorrect."
        if self.curr_function.update_B(tools.str_to_float(self.B_var.get())):
            self.update_plot()
        else:
            messagebox.showinfo(
                message="Error! Invalid B. Please enter new value.\n"
                + self.curr_function.description_B
            )
            self.B_var.set(self.curr_function.B)

    def update_x_low(self):
        "Validates and updates x lower. Displays error message if incorrect."
        if self.curr_function.update_x_lower(tools.str_to_float(self.xlow_var.get())):
            self.update_plot()
        else:
            messagebox.showinfo(
                message="Error! Invalid value. \nx lower must be less than x upper"
            )
            self.xlow_var.set(self.curr_function.x_lower)

    def update_x_up(self):
        "Validates and updates x upper. Displays error message if incorrect."
        if self.curr_function.update_x_upper(tools.str_to_float(self.xup_var.get())):
            self.update_plot()
        else:
            messagebox.showinfo(
                message="Error! Invalid value. \nx upper must be greater than x upper"
            )
            self.xup_var.set(self.curr_function.x_upper)

    def update_function(self, dropdown_var):
        "Updates the function defaults from dropdown"
        self.curr_function = self.functions[dropdown_var]()
        self.function_label.configure(text=self.curr_function.description_fx)

        self.A_var.set(self.curr_function.A)
        self.A_label.configure(text="A: " + self.curr_function.description_A)

        self.B_var.set(self.curr_function.B)
        self.B_label.configure(text="B: " + self.curr_function.description_B)

        self.xlow_var.set(self.curr_function.x_lower)
        self.xup_var.set(self.curr_function.x_upper)

        self.update_plot()

    def update_plot(self):
        "Updates the plot"
        self.ax.clear()
        self.ax.plot(
            self.curr_function.x_vect,
            self.curr_function.y_vect,
        )
        self.canvas.draw()


def run_gui():
    "Runs GUI and returns the app."
    root = tk.Tk()
    app = GUI(master=root)
    app.mainloop()
    return app


if __name__ == "__main__":
    run_gui()

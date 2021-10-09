#!/usr/bin/env python

from setuptools import setup

setup(
    name="basic_graph_viewer",
    version="0.1.0",
    description="Allows users to plot functions.",
    author="Gabrielle Kim",
    author_email="gabriellelindakim@gmail.com",
    python_requires=">=3.7.9",
    package_dir={"": "src"},
    packages=["basic_graph_viewer", "basic_graph_viewer.fx"],
    install_requires=["numpy", "matplotlib"],
    zip_safe=False,
    include_package_data=True,
)

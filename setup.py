#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="basic_graph_viewer",
    version="0.1.0",
    description="Allows users to plot functions.",
    author="Gabrielle Kim",
    author_email="gabriellelindakim@gmail.com",
    python_requires=">=3.9",
    package_dir={"": "src"},
    packages=["basic_graph_viewer"],
    install_requires=["numpy"],
    zip_safe=False,
    include_package_data=True,
)

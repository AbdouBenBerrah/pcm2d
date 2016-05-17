import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pcm2d",
    version = "0.0.0",
    author = "Olivier Farges",
    author_email = "olivier@olivier-farges.com",
    description = ("A code that estimates radiative properties of a PCM in 2D"),
    license = "CeCILL",
    keywords = "PCM",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['pcm2d', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: X11 Applications",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Physics"
    ],
)

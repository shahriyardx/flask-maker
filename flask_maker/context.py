import os
from contextlib import contextmanager
from .helpers import go_back, empty_folder


@contextmanager
def open_dir(name, back=True):
    """Opens a directory"""
    if not os.path.exists(name):
        os.mkdir(name)

    os.chdir(name)

    yield None

    if back:
        go_back()


@contextmanager
def make_dir(name, back=True, empty=True):
    """Makes a directory"""
    if not os.path.exists(name):
        os.mkdir(name)

    os.chdir(name)

    if empty:
        empty_folder(os.getcwd())

    if not empty and os.listdir(os.getcwd()):
        yield f"Directory {name} is not empty."
    else:
        yield None

    if back:
        go_back()

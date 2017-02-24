# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
#

"""
Tests for pathmanager.py
"""
# Standard library imports
import sys

# Test library imports
import pytest

# Local imports
from spyder.utils.fixtures import setup_pathmanager

def test_pathmanager(qtbot):
    """Run PathManager test"""
    pathmanager = setup_pathmanager(qtbot, None, pathlist=sys.path[:-10],
                                    ro_pathlist=sys.path[-10:])
    pathmanager.show()
    assert pathmanager


if __name__ == "__main__":
    pytest.main()

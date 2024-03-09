#!/usr/bin/python3

"""
Module for teste the console.
"""

import io
import sys
import unittest
import os
from models.engine.file_storage import FileStorage

class TestConsole(unittest.TestCase):
    """
    Defines the test cases for the AitBnB console.
    """

    def setUp(self) -> None:
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

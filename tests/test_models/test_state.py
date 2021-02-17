#!/usr/bin/python3
"""Unit tests for state.py"""
import unittest
from models.state import State
import uuid
import datetime


class TestState(unittest.TestCase):
    """unit test for state.py"""
    def test_state(self):
        """main tests for checking state class"""
        state1 = State()
        self.assertEqual(type(state1.name), str)

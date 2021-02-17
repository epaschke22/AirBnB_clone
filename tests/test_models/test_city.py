#!/usr/bin/python3
"""Unit tests for city.py"""
import unittest
from models.city import City
import uuid
import datetime


class TestCity(unittest.TestCase):
    """unit test for city.py"""
    def test_city(self):
        """main tests for checking city class"""
        city1 = City()
        self.assertEqual(type(city1.name), str)
        self.assertEqual(type(city1.state_id), str)

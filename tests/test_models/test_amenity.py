#!/usr/bin/python3
"""Unit tests for amenity.py"""
import unittest
from models.amenity import Amenity
import uuid
import datetime


class TestAmenity(unittest.TestCase):
    """unit test for amenity.py"""
    def test_amenity(self):
        """main tests for checking amenity class"""
        amenity1 = Amenity()
        self.assertEqual(type(amenity1.name), str)

#!/usr/bin/python3
"""Unit tests for place.py"""
import unittest
from models.place import Place
import uuid
import datetime


class TestPlace(unittest.TestCase):
    """unit test for place.py"""
    def test_place(self):
        """main tests for checking place class"""
        place1 = Place()
        self.assertEqual(type(place1.name), str)
        self.assertEqual(type(place1.city_id), str)
        self.assertEqual(type(place1.user_id), str)
        self.assertEqual(type(place1.description), str)
        self.assertEqual(type(place1.number_rooms), int)
        self.assertEqual(type(place1.number_bathrooms), int)
        self.assertEqual(type(place1.max_guest), int)
        self.assertEqual(type(place1.price_by_night), int)
        self.assertEqual(type(place1.latitude), float)
        self.assertEqual(type(place1.longitude), float)
        self.assertEqual(type(place1.amenity_ids), list)

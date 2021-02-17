#!/usr/bin/python3
"""Unit tests for review.py"""
import unittest
from models.review import Review
import uuid
import datetime


class TestReview(unittest.TestCase):
    """unit test for userreview.py"""
    def test_review(self):
        """main tests for checking review class"""
        review1 = Review()
        self.assertEqual(type(review1.place_id), str)
        self.assertEqual(type(review1.user_id), str)
        self.assertEqual(type(review1.text), str)

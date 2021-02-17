#!/usr/bin/python3
"""Unit tests for user.py"""
import unittest
from models.user import User
import uuid
import datetime


class TestUser(unittest.TestCase):
    """unit test for user.py"""
    def test_user(self):
        """main tests for checking user class"""
        user1 = User()
        self.assertEqual(type(user1.first_name), str)
        self.assertEqual(type(user1.last_name), str)
        self.assertEqual(type(user1.email), str)
        self.assertEqual(type(user1.password), str)

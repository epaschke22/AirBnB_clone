#!/usr/bin/python3
"""Unit tests for base model.py"""
import unittest
from models.base_model import BaseModel
import uuid
import datetime


class TestBaseModel(unittest.TestCase):
    """Testing base_model.py"""
    def test_basemodel_init(self):
        base1 = BaseModel()
        self.assertEqual(type(base1.created_at), datetime.datetime)
        self.assertEqual(type(base1.updated_at), datetime.datetime)
        self.assertEqual(type(base1.id), str)

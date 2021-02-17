#!/usr/bin/python3
"""Unit tests for base file_storage.py"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import uuid
import datetime


class TestFileStorage(unittest.TestCase):
    """Testing file_storage.py"""
    def setUp(self):
        """runs before each test"""
        FileStorage._FileStorage__objects = {}
    def test_filestroage_all(self):
        """creating and testing objects dictionary"""
        self.maxDiff = None
        _obj = {}
        base1 = BaseModel()
        base2 = BaseModel()
        _obj[base1.__class__.__name__ + '.' + base1.id] = base1
        _obj[base2.__class__.__name__ + '.' + base2.id] = base2
        self.assertDictEqual(_obj, models.storage.all())

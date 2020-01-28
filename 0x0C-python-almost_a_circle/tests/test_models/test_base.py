#!/usr/bin/python3
"""
Test for Base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Testing instance new Base """
    def test_id(self):
        """ test id """
        b1 = Base()
        self.assertEqual(b1.id, 5)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(89)
        self.assertEqual(b3.id, 89)
        b4 = Base()
        self.assertEqual(b4.id - 1, b2.id)
        b5 = Base()
        self.assertEqual(b4.id + 1, b5.id)
        b6 = Base(None)
        self.assertEqual(b6.id, b5.id + 1)
        b7 = Base("id")
        self.assertEqual(b7.id, "id")
        b8 = Base([1, 2])
        self.assertEqual(b8.id, [1, 2])
        b9 = Base(2)
        b9.id = 9
        self.assertEqual(b9.id, 9)
        b10 = Base(2)
        b10.id = "otro id"
        self.assertEqual(b10.id, "otro id")
        b11 = Base(float("nan"))
        self.assertNotEqual(b11.id, float("nan"))
        b15 = Base(float("inf"))
        self.assertEqual(b15.id, float("inf"))
        b16 = Base(memoryview(b'asdfg'))
        self.assertEqual(b16.id, memoryview(b'asdfg'))
        b17 = Base(frozenset({"a", "b"}))
        self.assertEqual(b17.id, frozenset({"a", "b"}))
        b18 = Base(False)
        self.assertEqual(b18.id, False)
        b19 = Base(complex(123))
        self.assertEqual(b19.id, complex(123))
        b20 = Base({"a": 12, "v": 32})
        self.assertEqual(b20.id, {"a": 12, "v": 32})
        b20 = Base(None)
        self.assertEqual(b20.id, 6)
        b12 = Rectangle(1, 1, 1, 1)
        self.assertEqual(b12.id, 7)
        b12 = Rectangle(1, 1, 1, 1, 99)
        self.assertEqual(b12.id, 99)
        b13 = Rectangle(1, 1, 1, 1, 100)
        self.assertEqual(b13.id, 100)
        b14 = Rectangle(1, 1, 1, 1)
        self.assertEqual(b14.id, 8)

    def test_create_cls(self):
        """ test create any class """
        r1 = Rectangle(5, 7, 3, 3, 9)
        r1_dic = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dic)
        self.assertEqual("[Rectangle] (9) 3/3 - 5/7", str(r2))
        r3 = Rectangle(5, 7, 3, 3, 9)
        r3_dic = r3.to_dictionary()
        r4 = Rectangle.create(**r3_dic)
        self.assertIsNot(r3, r4)
        s1 = Square(5, 3, 3, 9)
        s1_dic = s1.to_dictionary()
        s2 = Square.create(**s1_dic)
        self.assertEqual("[Square] (9) 3/3 - 5", str(s2))
        s3 = Square(5, 3, 3, 9)
        s3_dic = s3.to_dictionary()
        s4 = Square.create(**s3_dic)
        self.assertIsNot(s4, s3)

    def test_to_json_string(self):
        """ Test json string """
        list1 = [{"size": 1, "id": 1}]
        json_str = Square.to_json_string(list1)
        res = Square.from_json_string(json_str)
        self.assertEqual(res, list1)

        list1 = [{"width": 9, "id": 2, "height": 8}]
        json_str = Rectangle.to_json_string(list1)
        res = Rectangle.from_json_string(json_str)
        self.assertEqual(res, list1)

    def test_save_to_file(self):
        """ test save to file """
        save = Rectangle(2, 4, 0, 0, 67)
        Rectangle.save_to_file([save])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(save), str(list_rectangles_output[0]))

    #  def test_load_from_file(self):
        """ test load from file """


    #  def test_from_json_string(self):
        """ test from json string """

    #  def test_save_to_file_csv(self):
        """ test save to file csv """

    #  def test_load_from_file_csv(self):
        """ test load from file csv """

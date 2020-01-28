#!/usr/bin/python3
"""
Test for Rectangle class
"""
import unittest
from sys import stdout, __stdout__
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Put test"""

    def test_instance(self):
        """ Test Instance new Rectangle """
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 9, 24, 24, 24, 24, 24, 24)
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 98, 98, 98, 98, 98)

    def test_invalid_args(self):
        """ invalid args """
        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 89)
        with self.assertRaises(ValueError):
            r5 = Rectangle(98, -98)
        with self.assertRaises(TypeError):
            r6 = Rectangle(24, "20")
        with self.assertRaises(TypeError):
            r7 = Rectangle(209, [1, 2, 3, 4])

    def test_area(self):
        """ test method area """
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.area(), 1)
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.area(), 4)
        r1 = Rectangle(8, 40)
        r1.height = 10
        self.assertEqual(r1.area(), 80)

    def test_update_args(self):
        """ test update only args """
        r1 = Rectangle(10, 10)
        r1.update(89)
        capture = TestRectangle.capture_stdout(r1, "print")
        correct = "[Rectangle] (89) 0/0 - 10/10\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 29)
        capture = TestRectangle.capture_stdout(r1, "print")
        correct = "[Rectangle] (89) 10/10 - 29/10\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        capture = TestRectangle.capture_stdout(r1, "print")
        correct = "[Rectangle] (10) 10/10 - 10/10\n"
        self.assertEqual(correct, capture.getvalue())

    def test_update_kwargs(self):
        """ test update only kwargs """
        r2 = Rectangle(10, 10)
        r2.update(id=89)
        capture = TestRectangle.capture_stdout(r2, "print")
        correct = "[Rectangle] (89) 0/0 - 10/10\n"
        self.assertEqual(correct, capture.getvalue())
        r2 = Rectangle(10, 10, 10, 10, 10)
        r2.update(width=29, id=89)
        capture = TestRectangle.capture_stdout(r2, "print")
        correct = "[Rectangle] (89) 10/10 - 29/10\n"
        self.assertEqual(correct, capture.getvalue())
        r2 = Rectangle(10, 10, 10, 10, 10)
        r2.update()
        capture = TestRectangleT.capture_stdout(r2, "print")
        correct = "[Rectangle] (10) 10/10 - 10/10\n"
        self.assertEqual(correct, capture.getvalue())

    def test_display(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.display(), None)
        r1 = Rectangle(3, 1)
        self.assertEqual(r1.display(), None)
        r1 = Rectangle(1, 1)
        capture = TestRectangle.capture_stdout(r1, "display")
        correct = "#\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(1, 2)
        capture = TestRectangle.capture_stdout(r1, "display")
        correct = "#\n#\n"
        self.assertEqual(correct, capture.getvalue())

    def test_display_x_y(self):
        """ Test display with eje x and y """

        r4 = Rectangle(1, 1)
        self.assertEqual(r4.display(), None)
        r4 = Rectangle(3, 1)
        self.assertEqual(r4.display(), None)
        r4 = Rectangle(1, 1, 1, 1)
        capture = TestClassRectangle.capture_stdout(r4, "display")
        correct = "\n #\n"
        self.assertEqual(correct, capture.getvalue())
        r4 = Rectangle(1, 2, 2, 2)
        capture = TestClassRectangle.capture_stdout(r4, "display")
        correct = "\n\n  #\n  #\n"
        self.assertEqual(correct, capture.getvalue())

    def test_to_dictionary(self):
        """ test method to_dictionary """

        """ Comparer output """
        r1 = Rectangle(20, 32, 4, 5, 6)
        dic = {'id': 6, 'width': 20, 'height': 32, 'x': 4, 'y': 5}
        self.assertDictEqual(r1, dic)

        """ arg in method """
        r2 = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r2.to_dictionary(1)

    @staticmethod
    def capture_stdout(obj, method):
        """
        return the stdout by 'bdbaraban'
        """
        val = io.StringIO()
        stdout = val
        if method == "print":
            print(obj)
        else:
            obj.display()
        stdout = __stdout__
        return Val

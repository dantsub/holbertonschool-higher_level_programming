#!/usr/bin/python3
"""
Test for Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test Square class """

    def test_instance(self):
        """ Test Instance new Rectangle """
        with self.assertRaises(TypeError):
            r1 = Square()
        with self.assertRaises(TypeError):
            r2 = Square(10, 9, 24, 24, 24, 24, 24, 24)
        with self.assertRaises(TypeError):
            r3 = Square(10, 98, 98, 98, 98, 98)

    def test_invalid_args(self):
        """ invalid args """
        with self.assertRaises(ValueError):
            r4 = Square(0)
        with self.assertRaises(ValueError):
            r5 = Square(-98)
        with self.assertRaises(TypeError):
            r6 = Square("20")
        with self.assertRaises(TypeError):
            r7 = Square([1, 2, 3, 4])

    def test_area(self):
        """ test method area """
        r1 = Square(1)
        self.assertEqual(r1.area(), 1)
        r1 = Square(2)
        self.assertEqual(r1.area(), 4)
        r1 = Square(8)
        r1.height = 3
        self.assertEqual(r1.area(), 9)

    def test_update_args(self):
        """ test update only args """
        r1 = Square(10)
        r1.update(89)
        capture = TestClassRectangle.capture_stdout(r1, "print")
        correct = "[Square] (89) 0/0 - 10\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Square(10, 10, 10, 10)
        r1.update(89, 29)
        capture = TestClassRectangle.capture_stdout(r1, "print")
        correct = "[Square] (89) 10/10 - 29\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Square(10, 10, 10, 10)
        r1.update()
        capture = TestClassRectangle.capture_stdout(r1, "print")
        correct = "[Square] (10) 10/10 - 10\n"
        self.assertEqual(correct, capture.getvalue())

    def test_update_kwargs(self):
        """ test update only kwargs """

        r2 = Square(10)
        r2.update(id=89)
        capture = TestClassRectangle.capture_stdout(r2, "print")
        correct = "[Square] (89) 0/0 - 10\n"
        self.assertEqual(correct, capture.getvalue())
        r2 = Square(10, 10, 10)
        r2.update(width=29, id=89)
        capture = TestClassRectangle.capture_stdout(r2, "print")
        correct = "[Square] (89) 10/10 - 29\n"
        self.assertEqual(correct, capture.getvalue())
        r2 = Square(10, 10, 10)
        r2.update()
        capture = TestClassRectangle.capture_stdout(r2, "print")
        correct = "[Square] (10) 10/10 - 10\n"
        self.assertEqual(correct, capture.getvalue())

    def test_display(self):
        """ test method display """

        r1 = Square(1, 1)
        self.assertEqual(r1.display(), None)
        r1 = Square(3, 1)
        self.assertEqual(r1.display(), None)
        r1 = Square(1)
        capture = TestClassRectangle.capture_stdout(r1, "display")
        correct = "#\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Square(2)
        capture = TestClassRectangle.capture_stdout(r1, "display")
        correct = "##\n##\n"
        self.assertEqual(correct, capture.getvalue())

    def test_display_x_y(self):
        """ Test display with eje x and y """

        r4 = Square(1, 1)
        self.assertEqual(r4.display(), None)
        r4 = Square(3, 1)
        self.assertEqual(r4.display(), None)
        r4 = Square(1, 1, 1, 1)
        capture = TestClassRectangle.capture_stdout(r4, "display")
        correct = "\n #\n"
        self.assertEqual(correct, capture.getvalue())
        r4 = Square(1, 2, 2)
        capture = TestClassRectangle.capture_stdout(r4, "display")
        correct = "\n\n  #\n  #\n"
        self.assertEqual(correct, capture.getvalue())

    def test_to_dictionary(self):
        """ test method to_dictionary """

        """ Comparer output """
        r1 = Square(20, 4, 5, 6)
        dic = {'id': 6, 'size': 20, 'x': 4, 'y': 5}
        self.assertDictEqual(r1, dic)

        """ arg in method """
        r2 = Square(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r2.to_dictionary(1)

    @staticmethod
    def capture_stdout(obj, method):
        """
        return the stdout by 'bdbaraban'
        """
        ioVal = io.StringIO()
        stdout = ioVal
        if method == "print":
            print(obj)
        else:
            obj.display()
        stdout = __stdout__
        return ioVal

import unittest

from rectangle import Rectangle


class TestGetAreaRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(0, 0)

    def test_area_normal_case(self):
        self.rectangle.set_width(3)
        self.rectangle.set_height(2)
        self.assertEqual(self.rectangle.get_area(), 6, "incorrect area")

    def test_area_negative(self):
        self.rectangle.set_width(-1)
        self.rectangle.set_height(2)
        self.assertEqual(self.rectangle.get_area(), -1, "incorrect area")

    def test_perimeter_normal_case(self):
        self.rectangle.set_width(4)
        self.rectangle.set_height(3)
        self.assertEqual(self.rectangle.get_perimeter(), 14, "Incorrect perimeter for normal case")

    def test_perimeter_zero_case(self):
        self.rectangle.set_width(0)
        self.rectangle.set_height(0)
        self.assertEqual(self.rectangle.get_perimeter(), 0, "Incorrect perimeter when dimensions are zero")

if __name__ == "main":
    unittest.main()

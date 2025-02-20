import unittest
from app.Lab3_AlexS import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)
        self.assertAlmostEqual(circle_area(3.5), 38.48451000657496)
        self.assertEqual(circle_area(0), 0)
        

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)
        with self.assertRaises(ValueError):
            circle_area('h')

    def test_trapezium_area_valid(self):
        self.assertEqual(trapezium_area(4, 3, 2), 7)
        self.assertEqual(trapezium_area(0,0,0), 0)
        self.assertEqual(trapezium_area(4.5, 3.75, 2.25), 9.28125)
    
    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-4, 2, 1)
        with self.assertRaises(ValueError):
            trapezium_area(4, -2, 1)
        with self.assertRaises(ValueError):
            trapezium_area(4, 2, -1)
        with self.assertRaises(ValueError):
            trapezium_area('h', 2, 1)
        with self.assertRaises(ValueError):
            trapezium_area(4, 'g', 1)
        with self.assertRaises(ValueError):
            trapezium_area(4, 2, 'f')


    def test_ellipse_area_valid(self):
        self.assertAlmostEqual(ellipse_area(2, 4), 25.132741228718345)
        self.assertEqual(ellipse_area(0,0), 0)
        self.assertAlmostEqual(ellipse_area(7.5, 2.5), 58.90486225480862)

    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(-4, 0)
        with self.assertRaises(ValueError):
            ellipse_area(4, -4)
        with self.assertRaises(ValueError):
            ellipse_area('h', 4)
        with self.assertRaises(ValueError):
            ellipse_area(4, 'j')
    
    def test_rhombus_area_valid(self):
        self.assertEqual(rhombus_area(2,2), 2)
        self.assertEqual(rhombus_area(0,0), 0)
        self.assertEqual(rhombus_area(2.5, 2.5), 3.125)

    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(-2, 2)
        with self.assertRaises(ValueError):
            rhombus_area(2, -2)
        with self.assertRaises(ValueError):
            rhombus_area('k', 2)
        with self.assertRaises(ValueError):
            rhombus_area(2, 'l')


if __name__ == "__main__":
    unittest.main()
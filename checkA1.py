import os
import unittest
from assignment1 import day_of_week, leap_year, mon_max, after, before, valid_date, day_iter, day_count

class TestAfter(unittest.TestCase):
    def setUp(self):
        self.file = r'C:\Users\Dell\Desktop\ops445\assignment1\assignment1.py'
        self.error_output = f"{self.file} cannot be found (HINT: make sure this script AND your file are in the same directory)"
        self.assertTrue(os.path.exists(self.file), msg=self.error_output)

    def test_after_date(self):
        self.assertEqual(after("01/01/2024"), "02/01/2024")
        self.assertEqual(after("31/12/2024"), "01/01/2025")

class TestBefore(unittest.TestCase):
    def setUp(self):
        self.file = r'C:\Users\Dell\Desktop\ops445\assignment1\assignment1.py'
        self.error_output = f"{self.file} cannot be found (HINT: make sure this script AND your file are in the same directory)"
        self.assertTrue(os.path.exists(self.file), msg=self.error_output)

    def test_before_date(self):
        self.assertEqual(before("01/01/2024"), "31/12/2023")
        self.assertEqual(before("01/01/2025"), "31/12/2024")

class TestDayIter(unittest.TestCase):
    def setUp(self):
        self.file = r'C:\Users\Dell\Desktop\ops445\assignment1\assignment1.py'
        self.error_output = f"{self.file} cannot be found (HINT: make sure this script AND your file are in the same directory)"
        self.assertTrue(os.path.exists(self.file), msg=self.error_output)

    def test_day_iter(self):
        self.assertEqual(day_iter("01/01/2024", 10), "11/01/2024")
        self.assertEqual(day_iter("01/01/2024", -10), "22/12/2023")

class TestDayOfWeek(unittest.TestCase):
    def setUp(self):
        self.file = r'C:\Users\Dell\Desktop\ops445\assignment1\assignment1.py'
        self.error_output = f"{self.file} cannot be found (HINT: make sure this script AND your file are in the same directory)"
        self.assertTrue(os.path.exists(self.file), msg=self.error_output)

    def test_dow(self):
        self.assertEqual(day_of_week("01/01/2024"), "Mon")
        self.assertEqual(day_of_week("31/12/2024"), "Tue")

class TestLeap(unittest.TestCase):
    def setUp(self):
        self.file = r'C:\Users\Dell\Desktop\ops445\assignment1\assignment1.py'
        self.error_output = f"{self.file} cannot be found (HINT: make sure this script AND your file are in the same directory)"
        self.assertTrue(os.path.exists(self.file), msg=self.error_output)

    def test_leap_func(self):
        self.assertTrue(leap_year(2020))
        self.assertFalse(leap_year(2021))
        self.assertTrue(leap_year(2000))
        self.assertFalse(leap_year(1900))

class TestMonMax(unittest.TestCase):
    def setUp(self):
        self.file = r'C:\Users\Dell\Desktop\ops445\assignment1\assignment1.py'
        self.error_output = f"{self.file} cannot be found (HINT: make sure this script AND your file are in the same directory)"
        self.assertTrue(os.path.exists(self.file), msg=self.error_output)

    def test_mon_max(self):
        self.assertEqual(mon_max(2, 2024), 29)  # Leap year February
        self.assertEqual(mon_max(2, 2023), 28)  # Non-leap year February
        self.assertEqual(mon_max(4, 2024), 30)  # April
        self.assertEqual(mon_max(7, 2024), 31)  # July

class TestValidDate(unittest.TestCase):
    def setUp(self):
        self.file = r'C:\Users\Dell\Desktop\ops445\assignment1\assignment1.py'
        self.error_output = f"{self.file} cannot be found (HINT: make sure this script AND your file are in the same directory)"
        self.assertTrue(os.path.exists(self.file), msg=self.error_output)

    def test_valid_date(self):
        self.assertTrue(valid_date("01/01/2024"))
        self.assertFalse(valid_date("31/02/2024"))  # Invalid date
        self.assertFalse(valid_date("01/13/2024"))  # Invalid month

class TestDayCount(unittest.TestCase):
    def setUp(self):
        self.file = r'C:\Users\Dell\Desktop\ops445\assignment1\assignment1.py'
        self.error_output = f"{self.file} cannot be found (HINT: make sure this script AND your file are in the same directory)"
        self.assertTrue(os.path.exists(self.file), msg=self.error_output)

    def test_day_count(self):
        self.assertEqual(day_count("01/01/2024", "31/01/2024"), 30)
        self.assertEqual(day_count("01/01/2024", "01/01/2024"), 0)

class TestFinal(unittest.TestCase):
    def test_example(self):
        # Replace with actual final test cases
        self.assertEqual(day_of_week("01/01/2024"), "Mon")
        self.assertEqual(after("31/12/2024"), "01/01/2025")


if __name__ == '__main__':
    unittest.main()

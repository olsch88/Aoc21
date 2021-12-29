import unittest
import day25

class TestDay25(unittest.TestCase):
    
    def setUp(self): # Camel case required
        self.data = day25.read_data("25_sample.txt")
    
    def test_solve_part1(self):
        self.assertEqual(day25.solve_part1(self.data),58)
    
unittest.main()
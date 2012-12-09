import unittest
from game_of_life import *


"""class count_neighbours(unittest.TestCase):
    def setUp(self):
        self.universe = ([(2,2),(1,3),(3,3),(4,2),(4,1),(5,1)])

    def test_count(self):
        self.cell = (4,2)
        self.count = count_neighbours(self.cell,self.universe)
        self.assertEqual(self.count,3)
        #self.assertEqual(count_neighbours((3,3),universe),2,"Wrong Count, got %s" % count_neighbours((3,3),universe))
        #self.assertEqual(count_neighbours((1,3),universe),1,"Wrong Count, got %s" % count_neighbours((1,3),universe))"""

class moore_neighbourhood(unittest.TestCase):

    def test_get_moore_neighbourhood(self):
        expected = set([(1,1),(2,1),(3,1),(1,2),(3,2),(1,3),(2,3),(3,3)])
        self.assertSetEqual(get_moore_neighbourhood(2,2), expected, "got %s" % get_moore_neighbourhood(2,2))

class test_generations(unittest.TestCase):


    def test_survivors(self):
        input_pattern = set([(3,2),(3,3),(3,4)]) 
        expected = set([(3,3)])       
        self.assertSetEqual(get_survivors(input_pattern),expected, "failed, got %s" % get_survivors(input_pattern))

    def test_new_cells(self):
        input_pattern = set([(3,2),(3,3),(3,4)]) 
        expected = set([(2,3),(4,3)])       
        self.assertSetEqual(get_new_cells(input_pattern),expected, "failed, got %s" % get_new_cells(input_pattern))
        

class test_tick(unittest.TestCase):

    def test_output_type(self):
        # test that tick returns a set. Cos thats a thing now.
        universe = set()
        self.assertEqual(type(tick(universe)),type(universe))

class test_blinker(unittest.TestCase):
    
    def test_tick_blinker(self):
        # test ticks output set. For a blinker.
        input_pattern = set([(3,2),(3,3),(3,4)])
        expected_output = set([(2,3),(4,3),(3,3)])
        self.assertSetEqual(tick(input_pattern),expected_output, "failed, got %s" % tick(input_pattern))

class test_glider(unittest.TestCase):
    
    def test_tick_glider(self):
        # test ticks output for a left facing glider with a random cell miles away.

        glider_pattern = set([(5,4),(4,5),(4,6),(5,6),(6,6),(36,16)])
        expected_output = set([(4,5),(4,6),(5,6),(5,7),(6,5)])
        self.assertSetEqual(tick(glider_pattern),expected_output, "failed, got %s" % tick(glider_pattern))

if __name__ == "__main__":
    unittest.main()


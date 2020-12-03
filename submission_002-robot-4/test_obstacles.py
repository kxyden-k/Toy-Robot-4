import unittest
from world import obstacles

class Testobstacle(unittest.TestCase):
    def test_position_blocked_true(self):
        obstacles.obstacle_lst = [(26,53),(38,52)]
        self.assertTrue(obstacles.is_position_blocked(27,54))


    def test_position_blocked_false(self):
        obstacles.obstacle_lst = [(26,53),(38,52)]
        self.assertFalse(obstacles.is_position_blocked(21,54))
    

    def test_path_blocked_false(self):
        obstacles.obstacle_lst = [(26,53),(38,52)]
        self.assertFalse(obstacles.is_path_blocked(10,54,10,57))
        

    def test_path_blocked_true(self):
        obstacles.obstacle_lst = [(26,53),(38,52),(50,20)]
        self.assertTrue(obstacles.is_path_blocked(49,20,60,20))


    

if __name__ == "__main__":
    unittest.main()
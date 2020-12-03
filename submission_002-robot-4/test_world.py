import unittest
from unittest.mock import patch
from io import StringIO
import sys
from test_base import captured_io
from world.text import world
import robot
import world.obstacles as obstacles

class Test_world(unittest.TestCase):
    def test_forward(self):

        with captured_io(StringIO('Kay\nforward 10\noff\n')) as (out, err):
            obstacles.random.randint = lambda a,b: 0
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next?  > Kay moved forward by 10 steps.
 > Kay now at position (0,10).
Kay: What must I do next? Kay: Shutting down..""", output)


    def test_right(self):

        with captured_io(StringIO('Kay\nright\noff\n')) as (out, err):
            obstacles.random.randint = lambda a,b: 0
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""Kay: What must I do next?  > Kay turned right.
 > Kay now at position (0,0).
Kay: What must I do next? Kay: Shutting down..""", output[-123:])


    def test_left(self):

        with captured_io(StringIO('Kay\nleft\nforward 10\noff\n')) as (out, err):
            obstacles.random.randint = lambda a,b: 0
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""Kay: What must I do next?  > Kay turned left.
 > Kay now at position (0,0).
Kay: What must I do next?  > Kay moved forward by 10 steps.
 > Kay now at position (-10,0).
Kay: What must I do next? Kay: Shutting down..""", output[-214:])



    def test_back(self):

        with captured_io(StringIO('Kay\nback 10\noff\n')) as (out, err):
            obstacles.random.randint = lambda a,b: 0
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""Kay: What must I do next?  > Kay moved back by 10 steps.
 > Kay now at position (0,-10).
Kay: What must I do next? Kay: Shutting down..""", output[-135:])


    def test_sprint(self):

        with captured_io(StringIO('Kay\nsprint 5\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next?  > Kay moved forward by 5 steps.
 > Kay moved forward by 4 steps.
 > Kay moved forward by 3 steps.
 > Kay moved forward by 2 steps.
 > Kay moved forward by 1 steps.
 > Kay now at position (0,15).
Kay: What must I do next? Kay: Shutting down..""", output)


    def test_range(self):

        with captured_io(StringIO('Kay\nforward 201\nforward 10\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next? Kay: Sorry, I cannot go outside my safe zone.
 > Kay now at position (0,0).
Kay: What must I do next?  > Kay moved forward by 10 steps.
 > Kay now at position (0,10).
Kay: What must I do next? Kay: Shutting down..""", output)

if __name__ == "__main__":
    unittest.main()
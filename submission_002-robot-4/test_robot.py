import unittest
import robot
from unittest.mock import patch
from io import StringIO
import sys
from test_base import captured_io
import world.obstacles as obstacles

class Test_robot(unittest.TestCase):

    """used to test if the off function/command works accordingly"""
    def test_off_function(self):
        with captured_io(StringIO('Kay\nOfF\n')) as (out, err):
                obstacles.random.randint = lambda a, b: 0
                robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next? Kay: Shutting down..""", output)


    """used to test if the help function/command works accordingly"""
    def test_help(self):
        with captured_io(StringIO('Kay\nhElp\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]""", output[:515])


    def test_replay(self):
        with captured_io(StringIO('Kay\nforward 10\nreplay\noff\n')) as (out, err):
                obstacles.random.randint = lambda a, b: 0
                robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next?  > Kay moved forward by 10 steps.
 > Kay now at position (0,10).
Kay: What must I do next?  > Kay moved forward by 10 steps.
 > Kay now at position (0,20).
 > Kay replayed 1 commands.
 > Kay now at position (0,20).""",output[:295])

    def test_silent_replay(self):
        with captured_io(StringIO('Kay\nforward 10\nreplay silent\noff\n')) as (out, err):
                obstacles.random.randint = lambda a, b: 0
                robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual('''What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next?  > Kay moved forward by 10 steps.
 > Kay now at position (0,10).
Kay: What must I do next?  > Kay replayed 1 commands silently.
 > Kay now at position (0,20).''',output[:239])


    def test_replay_reversed(self):
        with captured_io(StringIO('Kay\nforward 10\nback 5\nreplay reversed\noff\n')) as (out, err):
                obstacles.random.randint = lambda a, b: 0
                robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual('''What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next?  > Kay moved forward by 10 steps.
 > Kay now at position (0,10).
Kay: What must I do next?  > Kay moved back by 5 steps.
 > Kay now at position (0,5).
Kay: What must I do next?  > Kay moved back by 5 steps.
 > Kay now at position (0,0).
 > Kay moved forward by 10 steps.
 > Kay now at position (0,10).
 > Kay replayed 2 commands in reverse.
 > Kay now at position (0,10).''',output[:452])


    def test_replay_reversed_silent(self):
        with captured_io(StringIO('Kay\nforward 10\nback 5\nreplay reversed silent\noff\n')) as (out, err):
                obstacles.random.randint = lambda a, b: 0
                robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual('''What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next?  > Kay moved forward by 10 steps.
 > Kay now at position (0,10).
Kay: What must I do next?  > Kay moved back by 5 steps.
 > Kay now at position (0,5).
Kay: What must I do next?  > Kay replayed 2 commands in reverse silently.
 > Kay now at position (0,10).''', output[:336])


    def test_replay_limit_range(self):
        with captured_io(StringIO('Kay\nback 3\nback 2\nback 1\nreplay 3-1\noff\n')) as (out, err):
                obstacles.random.randint = lambda a, b: 0
                robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual('''What do you want to name your robot? Kay: Hello kiddo!
Kay: What must I do next?  > Kay moved back by 3 steps.
 > Kay now at position (0,-3).
Kay: What must I do next?  > Kay moved back by 2 steps.
 > Kay now at position (0,-5).
Kay: What must I do next?  > Kay moved back by 1 steps.
 > Kay now at position (0,-6).
Kay: What must I do next?  > Kay moved back by 3 steps.
 > Kay now at position (0,-9).
 > Kay moved back by 2 steps.
 > Kay now at position (0,-11).
 > Kay replayed 2 commands.
 > Kay now at position (0,-11).
Kay: What must I do next? Kay: Shutting down..''',output)


if __name__ == "__main__":
    unittest.main()


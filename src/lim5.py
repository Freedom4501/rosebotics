"""
  Capstone Project.  Code written by Mashengjun Li.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    #run_tests()
    turning(1, 5)


def run_tests():
    """ Runs various tests. """
    run_test_go_stop()


def run_test_go_stop():
    """ Tests the   go   and   stop   Snatch3rRobot methods. """
    robot = rb.Snatch3rRobot()

    robot.go(50, 25)
    time.sleep(2)
    robot.stop()

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())
    robot.left_wheel.reset_degrees_spun(0)

    time.sleep(2)

    robot.go(100, 100)
    time.sleep(3)
    robot.stop(rb.StopAction.COAST.value)

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())

def turning(x, N):
    robot = rb.Snatch3rRobot()
    robot.left_wheel.start_spinning(x)
    robot.right_wheel.start_spinning(-x)
    time.sleep(N)
    robot.stop(rb.StopAction.COAST.value)


main()

"""
  Capstone Project.  Code written by Jiafan Lin.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    run_test_go_stop()
    run_test_spinning()


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

def run_test_spinning():
    robot = rb.Snatch3rRobot()
    robot.spinning(100,-100)
    robot.left_wheel.motor.duty_cycle

def spinning(robot,time_right,time_left):
    robot.right_wheel.start_spinning(time_right)
    robot.left_wheel.start_spinning(time_left)
    robot.right_wheel.stop_spinning(rb.StopAction.BRAKE.value)
    robot.left_wheel.stop_spinning(rb.StopAction.BRAKE.value)




main()

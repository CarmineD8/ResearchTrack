#!/usr/bin/env python

import robot

	
def main():
	robot_1 = robot.Robot("robot_1", 10)
	robot_2 = robot.Robot("robot_2", 20)
	robot_3 = robot.Robot("robot_3", 5)

	robot_1.speed_up(20)
	robot_2.speed_up(20)
	robot_3.speed_up(2)

	robot_3.slow_down(10)

main()


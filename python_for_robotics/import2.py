#!/usr/bin/env python

from robot import Robot

	
def main():
	robot_1 = Robot("robot_1", 10)
	robot_2 = Robot("robot_2", 20)
	robot_3 = Robot("robot_3", 5)

	robot_1.speed_up(20)
	robot_2.speed_up(20)
	robot_3.speed_up(2)

	robot_3.slow_down(10)

main()


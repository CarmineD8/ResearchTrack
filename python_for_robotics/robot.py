#!/usr/bin/env python

# Here is where we define the class named Robot
class Robot:

  #### Data ####
  # All classes have a function called __init__(),  which executes each time you create a new object 
  
    def __init__(self, name, max_speed):
	self.max_speed=max_speed
	self.speed=0
	self.name=name

  #### Functions ####
  # Function to speed up the robot by a certain amount
    def speed_up(self, speed_increase):
	self.speed += speed_increase
	if self.speed > self.max_speed:
	    self.speed = self.max_speed
	print(self.name + " speed is now " + str(self.speed) + " m/s")

  # Function to slow down the car by a certain amount.
    def slow_down(self, speed_decrease):
	self.speed -= speed_decrease
	if self.speed <-self.max_speed:
		self.speed = -self.max_speed
	print(self.name + " speed is now " + str(self.speed) + " m/s")


# Here is where we define the main function of the program.
def main():

  # The syntax below shows how to create an object of a class.
    robot_1 = Robot("robot_1", 10)
    robot_2 = Robot("robot_2", 20)
    robot_3 = Robot("robot_3", 5)

  # The syntax below shows how to call a function from an object.
    robot_1.speed_up(20)
    robot_2.speed_up(20)
    robot_3.speed_up(2)

  # Slow down robot 3 by 10 m/s
    robot_3.slow_down(10)

# Run the main function.
# Code execution starts (and ends) here.
main()

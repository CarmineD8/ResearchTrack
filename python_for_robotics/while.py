#!/usr/bin/env python

# The robot begins at the origin (x=0, y=0, and z=0)
robot_x = 0
robot_y = 0
robot_z = 0

# Print the robot's starting position
print("Current Position: x=" + str(robot_x) + " y=" + str(robot_y) + " z=" + str(robot_z))

# Stop executing code once either x, y, or z exceeds 5
while (robot_x < 5 or robot_y < 5 or robot_z < 5):
  # Increment the robot's x position by 1
  robot_x += 1
  # Increment the robot's y position by 1
  robot_y += 1
  # Increment the robot's z position by 1
  robot_z += 1
  # Print the robot's current position
  print("Current Position: x=" + str(robot_x) + " y=" + str(robot_y) + " z=" + str(robot_z))

print("Mission complete.")

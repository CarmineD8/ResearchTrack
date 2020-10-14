#!/usr/bin/env python

# Robot security guard for a nightclub

# Ask for the person's age
age = input("How old are you?: ")

# Make a decision based on the person's age
if age < 18:
  print("You may NOT enter")
  print("Goodbye")
else:
  print("You may enter")

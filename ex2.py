#!/usr/bin/env python3

# Exercise 2: Write a Boolean function that checks if a string contains ‘@’ sign and at least one ‘.’ dot (disregard the order for the sake of simplicity). Use that function to check if a user input is a valid e-mail or not.

email = str(input("Enter a valid email:"))
if '@' in email and '.' in email:
    print("The email address is valid")
else:
    print("The email address is not valid")

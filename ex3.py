#!/usr/bin/env python3

# Exercise 3: 3. Guessing game! Pick a number randomly. While user does not guess the number correctly give an instruction about the number and take another guess from user.

import random
num = random.randint(1,1000)
guess = int(input("Please enter an integer number:"))
while num != guess:
    if num > guess:
        print("Please increase your number")
    else:
        print("Please decrease your number")
    guess = int(input("Please enter your new guess:"))
print("Your guess is correct!")

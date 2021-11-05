#!/usr/bin/env python3

# Exercise 1: Write a program that asks for a number N as a user input, and calculates the sum of odd numbers, and the average of even numbers starting from 1 up to and including N.

n = int(input("Enter a number:"))
sum_of_odds = 0
sum_of_evens = 0
for i in range (n+1):
    if i % 2 == 0:
        sum_of_evens += i
    else:
        sum_of_odds += i

avg_of_evens = sum_of_evens / n
print("Sum of odd numbers:", sum_of_odds)      
print("Average of even numbers:", avg_of_evens)

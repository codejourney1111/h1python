"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

"""




#!/bin/python

def check(number):
    number1 = number % 2
    if number1 != 0:
        print "Weird"

    else:
        if 2 < number < 5:
            print ('Not Weird')
        elif 6 <= number <= 20:
            print ('Weird')
        elif number > 20:
            print ('Not Weird')


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
check(N)

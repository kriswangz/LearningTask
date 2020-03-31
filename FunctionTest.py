# Lesson 2
# function test, like while, for, list and import.

# print  sin value of number 0-9 in a list table.
import math

# define a sine calculation function.
def sin_cal(index):
    sin_output = math.sin(index)
    print(sin_output)

list = [0,1,2,3,4,5,6,7,8,9] # init a list table
for i  in range(len(list)):
    print(sin_cal(list[i]))
    
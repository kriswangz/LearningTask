#!/usr/bin/python
# -*- coding: utf-8 -*-
# The program is used for solving josephus promblem.
# character:
#           n: total numbers
#           k: step value
# description:
#           Counting from the first person, when count to the step value, he must commit suicide, 
#           and then report again from the next, until everyone suicide.
# Author: Chris Wang


def josephus(total, step, start = 0):
    
    n = len(total)
    if n == 1:
        return total[0]

    p = start       # index point
    for i in range(n):
        if len(total) == 1:
            break

        p = (p + (step - 1)) % len(total)

        del total[p]
    return total[0]

total = []
n = 1
step = 2
for i in range(1, n+1):
    total.append(i)

survive = josephus(total, step)
print("survive:",survive)
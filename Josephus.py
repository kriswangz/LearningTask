#!/usr/bin/python
# -*- coding: utf-8 -*-

# The program is used for solving josephus promblem.
# character:
#           total: total chars, names included.
#           step: step value.
#           start: start point.
# description:
#           Counting from the first person, when count to the step value, he must commit suicide, 
#           and then report again from the next, until everyone suicide.
# Author: Chris Wang
class Josephus:
    def __init__(self, total, step, start):
        self.total = total
        self.step = step
        self.start = start
    
    def judge_survive(self):
        n = int(len(self.total))

        if n == 1:
            return self.total[0]

        p = self.start       # index point
        for i in range(n):
            if len(self.total) == 1:
                break

            p = (p + (self.step - 1)) % len(self.total)
            self.total.pop(p)

        return self.total[0]     #return survive people's index.

total = ["Chris", "Anna", "Bob", "David"]
step = 1
start = 0

joseph = Josephus(total, step, start)
survive = joseph.judge_survive()
print("survive:",survive)

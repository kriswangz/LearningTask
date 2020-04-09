#!/usr/bin/python
# -*- coding: utf-8 -*-

# The program is used for solving josephus promblem.
# character:
#           name: total characters, names included.
#           step: step value.
#           start: start point.
# description:
#           Counting from the first person, when count to the step value, he must commit suicide, 
#           and then report again from the next, until everyone suicide.
# Author: Chris Wang
class Josephus:
    def __init__(self, name, step, start):
        self.name = name
        self.step = step
        self.start = start
    
    def judge_survive(self):
        length = int(len(self.name))

        if length == 1:
            return self.name[0]

        p = self.start       # index point
        for i in range(length):
            if len(self.name) == 1:
                break

            p = (p + (self.step - 1)) % len(self.name)
            self.name.pop(p)

        return self.name[0]     #return survive people's index.

name = ["Chris", "Anna", "Bob", "David"]
step = 1
start = 0

joseph = Josephus(name, step, start)
survive = joseph.judge_survive()
print("survive:",survive)

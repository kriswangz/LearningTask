# %%
#!/usr/bin/python
# -*- coding: utf-8 -*-

# The program is used for solving josephus promblem.
# character:
#           name: total characters, names included.
#           step: step value.
#           start: start point.
# description:
#           Counting from the first person, when count to the step value, he must commit suicide, 
#           and then report again from the next, until the last one.
# Author: Chris Wang

class Josephus:
    """
    input rings([0,1..n]), this class will output the survivor index numbers in rings.
    """
    def __init__(self, rings, step, start):
        self.rings = rings
        self.step = step
        self.start = start

    def judge_survive(self):
        p = self.start       # index point

        for i in range(len(self.rings)):
            if len(self.rings) == 1:
                break

            p = (p + (self.step - 1)) % len(self.rings)
            self.rings.pop(p)

        return self.rings[0]     #return survive people's index.

class  CreateRings:
    """
    convert name items to rings, use numbers instead of complex characters like dictionary
    """
    def __init__(self, name):
        self.name = name
    
    def create_rings(self):
        length = int(len(self.name))

        if length == 1:
            return [0]
        
        self.rings = [i for i in range(length)]

        return self.rings

name = {0:['Chris','24'], 1:['Anna','18'], 3:["Bob",'30'], 4:["David",'21']}
step = 2
start = 0

rings = CreateRings(name)
ring = rings.create_rings()  # generate rings [0..n] n=len(name)

joseph = Josephus(ring, step, start)
survive = joseph.judge_survive() # return index value in rings
print("survive is %s, age is %s" %(name[survive][0],name[survive][1]))

# %%
#!/usr/bin/python3
# -*- coding: utf-8 -*-

# The program is used for solving josephus promblem.
# description:
#           Counting from the first person, when count to the step value, he must commit suicide,
#           and then report again from the next, until the last one.
# Author: Chris Wang


class Ring(object):
    """
     this class is used for solving Josephus problem.

    """

    def __init__(self):
        self.start = 0
        self.step = 1
        self.people = []
        self.temp = []

    def append(self, index):
        self.people.append(index)
        return self.people

    def pop(self, index):
        self.people.pop(index)
        return self.people

    def remove_src(self, src):
        self.people.pop(src)
        return self.people

    def query_list_all(self):
        return self.people

    def query_list_one(self, index):
        return self.people[index]

    def reset(self):
        self.current_id = self.start
        self.temp = self.people
        return

    def kill_next(self):
        self.temp = self.people
        size = len(self.temp)
        if(size == 0):
            return None
        _id = (self.current_id + self.step - 1) % (size)
        res = self.temp.pop(_id)
        return res


ring = Ring()
ring.start = 0
ring.step = 4
ring.append(['chris', '24', 'male'])
ring.append(['Anna', '20', 'femal'])
ring.append(['Bob', '30', 'male'])
ring.append(['David', '20', 'male'])

ring.reset()

res = ring.query_list_all()
size_res = len(res)
for i in range(size_res):
    some_one = ring.kill_next()
    if some_one == None:
        break
    if i == size_res - 1:
        print("Survivor's name is %s, age is %s, gender is %s" %
              (some_one[0], some_one[1], some_one[2]))

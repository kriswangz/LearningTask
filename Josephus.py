# %%
#!/usr/bin/python3
# -*- coding: utf-8 -*-

# The program is used for solving josephus promblem.
# description:
#           Counting from the first person, when count to the step value, he must commit suicide,
#           and then report again from the next, until the last one.
# Author: Chris Wang
import csv
import os
import os.path
import fileinput
import zipfile
import copy


class Ring(object):
    """
     this class is used for solving Josephus problem.

    """

    def __init__(self):
        self.start = 0
        self.step = 1
        self.__people = []
        self.__temp = []

    def __str__(self):
        return len(self.__people)

    def append(self, index):
        self.__people.append(index)
        return self.__people

    def pop(self, index):
        self.__people.pop(index)
        return self.__people

    def remove_src(self, src):
        self.__people.pop(src)
        return self.__people

    def query_list_all(self):
        return self.__people

    def query_list_one(self, index):
        return self.__people[index]

    def reset(self):
        self.__current_id = self.start
        self.__temp = copy.deepcopy(self.__people)
        return

    def kill_next(self):
        size = len(self.__temp)
        if(size == 0):
            return None
        id_ = (self.__current_id + self.step - 1) % (size)
        res = self.temp.pop(id_)
        return res

    def iter(self):
        temp = copy.deepcopy(self.__people)
        size = len(temp)
        start = copy.deepcopy(self.start)
        step = copy.deepcopy(self.step)
        if(size == 0):
            return None
        while True:
            id_ = (start + step - 1) % (size)
            res = temp.pop(id_)
            yield res


def read_csv(dirctory, mode):
    cache = []
    with open(dirctory, mode) as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            cache.append(row)
        cache.pop(0)          # delete the first line(not used)
        return cache


def read_txt(dirctory, mode):
    cache = []
    with open(dirctory, mode) as fp:
        read_txt = fp.readlines()
        for row in read_txt:
            row = row.strip('\n')   # delete '\n'
            # convert 1-dio list to 2-dio list like [, , ,]  -->>  [[,], [,], [,]]
            row = row.split(',')
            cache.append(row)
        cache.pop(0)          # delete the first line
        return cache


if __name__ == '__main__':
    people_data = read_txt('./data/people.txt', 'r')

    ring = Ring()                   # init a ring
    ring.start = 0
    ring.step = 1

    for row in people_data:             # add list in a ring
        ring.append(row)

    ring.reset()

    res = ring.query_list_all()

    size_res = len(res)
    # for i in range(size_res):
    #     some_one = ring.kill_next()

    generator = ring.iter()
    for i in range(size_res):
        some_one = next(generator)
        if some_one == None:
            break
        if i == size_res - 1:
            print("Survivor's name is %s, age is %s, gender is %s" %
                  (some_one[0], some_one[1], some_one[2]))
        else:
            continue

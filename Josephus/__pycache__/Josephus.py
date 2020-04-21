# %%
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
The program is used for solving josephus promblem.

description:
        Counting from the first person, when count to the step value, he must commit suicide,
        and then report again from the next, until the last one.
    
Author: Chris Wang
"""
import sys
sys.path.append('./read_file')

import read_file
import copy
import zipfile
import fileinput
import os



class Person(object):
    """
    create person class.
    """

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Ring(object):
    """
     this class is used for solving Josephus problem.
    """

    def __init__(self):
        self.start = 0
        self.step = 1
        self.__people = []
        self.__temp = []        # stage people list.

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

        if(size == 0):
            return None
        id_ = (self.__current_id + self.step - 1) % (len(self.__temp))
        res = self.__temp.pop(id_)

        return res

    def iter(self):
        temp = copy.deepcopy(self.__people)
        size = len(temp)
        id_ = self.start

        if(size == 0):
            return None

        for i in range(size):
            id_ = (id_ + self.step - 1) % (len(temp))
            res = temp.pop(id_)
            yield res


"""
    The format of each object should correspond to the parameters,
    the object should contain a total of 3 parameters name, age, gender.
    Each line reads the order of participants from the file,
    which is create_person in the order of name, age, gender.
"""


def create_person(name, age, gender):

    obj = Person(name, age, gender)
    obj.name = name
    obj.age = age
    obj.gender = gender

    return obj

if __name__ == '__main__':
    # people_data = read_data(Read_txt(), './data', 'people.txt', 'r')
    # people_data = read_data(Read_csv(), './data', 'people.txt', 'r')
    people_data = read_file.read_data(
        read_file.Read_zip(), './data/data.zip', 'people.txt', 'r')
    
    people_data.pop(0)  # delete first line(not used).
    print("Total person:", people_data)
    
    ring = Ring()               # init a ring class.
    ring.start = 0
    ring.step = 2

    for row in range(len(people_data)):
        # add list in a ring.
        ring.append(create_person(
            people_data[row][0], people_data[row][1], people_data[row][2]))

    ring.reset()

    res = ring.query_list_all()
    size_res = len(res)         # for iter loops.

    generator = ring.iter()     # create iter, decrease the use of memory.

    for i in range(size_res):

        some_one = next(generator)

        if some_one == None:
            break

        if i == size_res - 1:
            print("Survivor's name is %s, age is %s, gender is %s" %
                  (some_one.name, some_one.age, some_one.gender))
        else:
            continue

# %%
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
The program is used for solving josephus promblem.

description:
        Counting from the first person, when count to the step value, he must commit suicide,
        and then report again from the next, until the last one.
    
Author: Chris Wang.
"""
import os
import fileinput
import zipfile
import copy
import sys
import read_file
import csv


class Person(object):
    """
    create person class.
    """

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Ring:
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

    def append(self, obj):
        self.__people.append(obj)

    def pop(self, index):
        self.__people.pop(index)

    def remove_src(self, src):
        self.__people.pop(src)

    def query_list_all(self):
        return self.__people

    def query_list_one(self, index):
        return self.__people[index]


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

    @classmethod
    def create_from_txt_csv(cls, path, filename, mode):
        obj = cls()

        with open(path + '/' + filename, mode) as fp:
            read_txt = fp.readlines()

            for row in read_txt:
                row = read_file.str2list_row(row)
    
                obj.append(Person(row[0], row[1], row[2]))

        return obj

    @classmethod
    def create_from_zip(cls, path, filename, mode):
        obj = cls()

        with zipfile.ZipFile(path, mode) as z:

            namelist = z.namelist()
            if filename not in namelist:
                raise FileNotFoundError

            # get files suffix and judge.
            filename_split = filename.split('.')
            split_len = len(filename_split)
            filename_suffix = filename_split[split_len - 1]

            if filename_suffix == 'txt' or 'csv':
                fp = z.open(filename)
                read_txt = fp.readlines()
                fp.close()

                for row in read_txt:
                    row = bytes.decode(row)
                    row = read_file.str2list_row(row)
                    obj.append(Person(row[0], row[1], row[2]))
            else:
                raise FileExistsError

        return obj


"""
    The format of each object should correspond to the parameters,
    the object should contain a total of 3 parameters name, age, gender.
    Each line reads the order of participants from the file,
    which is create_person in the order of name, age, gender.
"""


if __name__ == '__main__':
    ring = Ring.create_from_txt_csv('./data', 'people.txt', 'r')
    #ring = Ring.create_from_zip('./data/data.zip', 'people.txt', 'r')
    ring.start = 0
    ring.step = 2

    ring.pop(0)                 #删除第0行的无用数据
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

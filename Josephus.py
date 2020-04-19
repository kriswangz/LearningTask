# %%
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
The program is used for solving josephus promblem.

description:
        Counting from the first person, when count to the step value, he must commit suicide,
        and then report again from the next, until the last one.
        
        people's characters like name, age and gender is saved in  txt, csv and zip files,
        program can use read_data to extract data and create josephus rings, judge who is
        the survivor.
        
        read_data's input type is below:

        data = read_data([obj], [path], [filename], [mode])

        obj: Read_txt  Read_csv   Read_zip 
        path: Relative path and absolute path are supported. 
                In particular, when reading zip files, path should add ./[filename].zip
                into your path.
        filename: [filename].txt   [filename].csv , others type are not supported.

        mode: read only in general. 

        Author: Chris Wang
"""

import csv
import os
import os.path
import fileinput
import zipfile
import copy


class Person(object):
    """
    create person class
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

# The format of each object should correspond to the parameters,
# the object should contain a total of 3 parameters name, age, gender.
# Each line reads the order of participants from the file,
# which is create_person in the order of name, age, gender.


def create_person(name, age, gender):

    obj = Person(name, age, gender)
    obj.name = name
    obj.age = age
    obj.gender = gender

    return obj


class Read_file(object):
    """
    interface class, for smooth reading.
    """

    def read(self, path, filename, mode='r'):
        raise NotImplementedError


def str2list_row(row):
    """
    convert 1-dio list to 2-dio list like [, , ,]  -->>  [[,], [,], [,]]
    """
    row = row.strip('\n')   # delete '\n'
    row = row.strip('\r')   # delete '\r'
    row = row.split(',')

    return row


class Read_csv(Read_file):

    def read(self, path, filename, mode='r'):
        cache = []
        with open(path + '/' + filename, mode) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')

            for row in read_csv:
                cache.append(row)
            cache.pop(0)          # delete the first line(not used)

        return cache


class Read_txt(Read_file):

    def read(self, path, filename, mode='r'):
        cache = []
        with open(path + '/' + filename, mode) as fp:
            read_txt = fp.readlines()

            for row in read_txt:
                row = str2list_row(row)
                cache.append(row)
            cache.pop(0)          # delete the first line

        return cache


class Read_zip(Read_file):
    """
    only read .csv and .txt files function in zip files is supported.
    if u wanna support more file types, please add your program in 
    this read definition.
    """
    def read(self, path, filename, mode='r'):
        cache = []
        with zipfile.ZipFile(path, mode) as z:

            namelist = z.namelist()
            if filename not in namelist:
                raise FileNotFoundError

            # get files suffix and judge
            filename_split = filename.split('.')
            split_len = len(filename_split)
            filename_suffix = filename_split[split_len - 1]

            if filename_suffix == 'txt' or 'csv':
                fp = z.open(filename)
                read_txt = fp.readlines()
                fp.close()

                for row in read_txt:
                    row = bytes.decode(row)
                    row = str2list_row(row)
                    cache.append(row)
                cache.pop(0)
            else:
                raise FileExistsError

        return cache


def read_data(file_obj, path, filename, mode):
    cache = []
    cache = file_obj.read(path, filename, mode)
    return cache


if __name__ == '__main__':
    # people_data = read_data(Read_txt(), './data', 'people.txt', 'r')
    # people_data = read_data(Read_csv(), './data', 'people.txt', 'r')
    people_data = read_data(
        Read_zip(), './data/data.zip', 'people.txt', 'r')

    ring = Ring()               # init a ring
    ring.start = 0
    ring.step = 1

    for row in range(len(people_data)):
        # add list in a ring
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

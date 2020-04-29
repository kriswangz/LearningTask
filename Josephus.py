'''
@Author: Chris Wang
@Date: 2020-04-27 01:59:21
@LastEditTime: 2020-04-29 09:57:49
>>>>>>> 5321aa6be8aeaeb5eadbfed02c9af9863808967a
@LastEditors: Please set LastEditors
@Description: Solve Josephus problem. Counting from the first person, 
            when count to the step value, he must commit suicide,
            and then report again from the next, until the last one.
@FilePath: \LearningTask\Josephus.py
'''
# %%
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import fileinput
import zipfile
import copy
import sys
import csv

'''
@description: return object, one object indicates one person,
            included name, age and gender.
@param {name, age, gender} 
@return: object
'''


class Person(object):

    def __init__(self, name='', age='', gender=''):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def create_from_reader(cls, item, is_list=False):
        obj = cls()

        if is_list:
            item = item.strip().split(',')

        obj.name = item[0]
        obj.age = item[1]
        obj.gender = item[2]

        return obj


'''
@description: used for solving Josephus problem.
            There are 2 ways for updating ring's items(self._people).
            solution1: Ring.create_from_txt_csv and Ring.create_from_zip, return object.
            solution2: use reader. reader is a container which saves people's data.
@param {reader, is_list} 
@yield: one person object
'''


class Ring(object):

    MAX_DEPTH = 100

    # reader is a general container which can save
    # list or str data. But the josephus ring class need list
    # data, so is_list is needed.
    def __init__(self, reader=None, is_list=False):
        self.start = 0
        self.step = 1
        self._people = []
        self._temp = []        # stage people list.

        if reader:
            for row in reader:
                self._people.append(Person.create_from_reader(row, is_list))

    def __str__(self):
        return str(len(self._people))

    def __len__(self):
        return len(self._people)

    def append(self, obj):
        if len(self._people) > Ring.MAX_DEPTH:
            raise Exception('Out of range')
        else:
            self._people.append(obj)

    def pop(self, index):
        self._people.pop(index)

    def remove_src(self, src):
        self._people.pop(src)

    def query_list_all(self):
        return self._people

    def query_list_one(self, index):
        return self._people[index]

    def iter(self):
        temp = copy.deepcopy(self._people)
        size = len(temp)
        id_ = self.start

        while size != 0:
            id_ = (id_ + self.step - 1) % (len(temp))
            res = temp.pop(id_)
            yield res

    @classmethod
    def create_from_txt_csv(cls, path, filename, mode):
        obj = cls()

        with open(path + '/' + filename, mode) as fp:
            read_txt = fp.readlines()

            for row in read_txt:
                row = str2list_row(row)

                obj.append(Person(name=row[1], age=row[0], gender=row[2]))

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
                    row = str2list_row(row)
                    obj.append(Person(name=row[0], age=row[1], gender=row[2]))
            else:
                raise FileExistsError

        return obj

class Read_file(object):
    """
    interface class, for smooth reading.
    """

    def read(self, path, filename, mode='r'):
        raise NotImplementedError


class Read_csv(Read_file):

    def read(self, path, filename, mode='r'):
        cache = []
        with open(path + '/' + filename, mode) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')

            for row in read_csv:
                cache.append(row)

        return cache


class Read_txt(Read_file):

    def read(self, path, filename, mode='r'):
        cache = []
        with open(path + '/' + filename, mode) as fp:
            read_txt = fp.readlines()

            for row in read_txt:
                row = str2list_row(row)
                cache.append(row)

        return cache


class Read_zip(Read_file):
    """
    only read .csv and .txt files function in zip files is supported.
    if u wanna support more file types, please add your program in 
    this class.
    """

    def read(self, path, filename, mode='r'):
        cache = []
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
                    row = str2list_row(row)
                    cache.append(row)
            else:
                raise FileExistsError

        return cache


def read_from_files(file_obj, path, filename, mode):
    cache = []
    cache = file_obj.read(path, filename, mode)
    return cache


def str2list_row(row):
    """
    convert str to list in a row.
    """
    row = row.strip('\n')   # delete '\n'.
    row = row.strip('\r')   # delete '\r'.
    row = row.split(',')

    return row


"""
    The format of each object should correspond to the parameters,
    the object should contain a total of 3 parameters name, age, gender.
    Each line reads the order of participants from the file,
    which is create_person in the order of name, age, gender.
"""

if __name__ == '__main__':

 
    reader = read_from_files(
        Read_csv(), './data', 'people.csv', 'r')
    ring = Ring(reader, is_list=False)  # read file类中读取的数据已经进行了格式转换，变为list

    ring.start = 0
    ring.step = 1

    ring.pop(0)                 # line[0]'s data is not effective data.

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

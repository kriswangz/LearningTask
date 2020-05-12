
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#实体主要完成的是约瑟夫环的创建，调用Person类中的reader
#或者shared中的读取数据接口进行约瑟夫环的创建。

# Description: Solve Josephus problem. Counting from the first person, 
#             when count to the step value, he must commit suicide,
#             and then report again from the next, until the last one.
# FilePath: \LearningTask\Josephus.py
# Author  : Chris Wang.



import os
import copy
import sys
import zipfile

from josephus.file_adapter import read_files
from josephus.person import person

# description: return object, one object indicates one person,
#             included name, age and gender.




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
    def __init__(self, reader=None):
        self.start = 0
        self.step = 1
        self._people = []
        self._temp = []        # stage people list.

        if reader:
            for row in reader:
                self._people.append(person.Person.create_from_reader(row))

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
                row = read_files.str2list_row(row)

                obj.append(person.Person(name=row[1], age=row[0], gender=row[2]))

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
                    row = read_files.str2list_row(row)
                    obj.append(person.Person(name=row[0], age=row[1], gender=row[2]))
            else:
                raise FileExistsError

        return obj




def read_from_files(file_obj, path, filename, mode):
    cache = []
    cache = file_obj.read(path, filename, mode)
    return cache

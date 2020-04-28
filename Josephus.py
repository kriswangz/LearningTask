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
    return object, one obkect indicates one person,
    included name, age and gender.
    """

    def __init__(self, name = '', age = '', gender = ''):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def create_from_reader(cls, item, is_list = False):
        obj = cls()

        if is_list:
            item = item.strip().split(',')

        obj.name = item[0]
        obj.age = item[1]
        obj.gender = item[2]

        return obj


class Ring:
    """
     this class is used for solving Josephus problem.
    """
    MAX_DEPTH = 100

    # reader is a general container, indicates it can save 
    # list or str data. But the jophusring class need list 
    # data, so is_list is needed.
    def __init__(self, reader = None, is_list = False):
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
        if len(self._people) > Ring.MAX_DEPTH :
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
                row = read_file.str2list_row(row)

                obj.append(Person(name = row[1], age = row[0], gender = row[2]))

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
                    obj.append(Person(name = row[0], age = row[1], gender = row[2]))
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
    #######################################################################
    # there are 3 ways for generating josephus ring.

    # solution 1:
    # ring = Ring.create_from_txt_csv('./data', 'people.txt', 'r')
    # ring = Ring.create_from_zip('./data/data.zip', 'people.txt', 'r')

    # solution 2: read_file module inlcuded Read_csv, Read_txt, Read_zip.
    # see more detials in read_file.py.
    reader = read_file.read_data(
        read_file.Read_csv(), './data', 'people.csv', 'r')
    ring = Ring(reader, is_list = False)  # read file类中读取的数据已经进行了格式转换，变为list

    # solution3 :
    # with open('./data/people.csv', 'r') as reader:

    #     ring = Ring(reader, is_list = True)  

########################################################################
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

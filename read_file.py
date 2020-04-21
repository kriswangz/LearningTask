# %%
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
people's characters like name, age and gender is saved in  txt, csv and zip files,
program can use read_data to extract data and create josephus rings, judge who is
the survivor.

read_data's input type is below:

    data = read_data([obj], [path], [filename], [mode])

    obj: Read_txt  Read_csv   Read_zip 

    path: Relative path and absolute path are supported. 
            In particular, when reading zip files, path should add ./[filename].zip.
            
    filename: [filename].txt   [filename].csv , others type are not supported.

    mode: read only in general. 

Author: Chris Wang
"""
import csv
import zipfile


class Read_file(object):
    """
    interface class, for smooth reading.
    """

    def read(self, path, filename, mode='r'):
        raise NotImplementedError


def str2list_row(row):
    """
    convert str to list in a row.
    """
    row = row.strip('\n')   # delete '\n'.
    row = row.strip('\r')   # delete '\r'.
    row = row.split(',')

    return row


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


def read_data(file_obj, path, filename, mode):
    cache = []
    cache = file_obj.read(path, filename, mode)
    return cache


from josephus.person.readfiles import ReadFiles
import csv
import zipfile

# implement subclass of ReadFIles class in person/readfiles.py
class ReadCSV(object):

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def read(self, mode='r'):
        cache = []
        with open(self.path + '/' + self.filename, mode) as csv_file:
            read_csv = csv.reader(csv_file, delimiter=',')

            for row in read_csv:
                cache.append(row)

        return cache

ReadFiles.register(ReadCSV)

class ReadTXT(object):

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def read(self, mode='r'):
        cache = []
        with open(self.path + '/' + self.filename, mode) as fp:
            read_txt = fp.readlines()

            for row in read_txt:
                row = str2list_row(row)
                cache.append(row)

        return cache

ReadFiles.register(ReadTXT)

class ReadZIP(ReadFiles):
    """
    only read .csv and .txt files function in zip files is supported.
    if u wanna support more file types, please add your program in 
    this class.
    """
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def read(self,  mode='r'):
        cache = []
        with zipfile.ZipFile(self.path, mode) as z:

            namelist = z.namelist()
            if self.filename not in namelist:
                raise FileNotFoundError

            # get files suffix and judge.
            filename_split = self.filename.split('.')
            split_len = len(filename_split)
            filename_suffix = filename_split[split_len - 1]

            if filename_suffix == 'txt' or 'csv':
                fp = z.open(self.filename)
                read_txt = fp.readlines()
                fp.close()

                for row in read_txt:
                    row = bytes.decode(row)
                    row = str2list_row(row)
                    cache.append(row)
            else:
                raise FileExistsError

        return cache

ReadFiles.register(ReadZIP)

def str2list_row(row):
    """
    convert str to list in a row.
    """
    row = row.strip('\n')   # delete '\n'.
    row = row.strip('\r')   # delete '\r'.
    row = row.split(',')

    return row
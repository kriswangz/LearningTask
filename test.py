
#%%
class ZFile(object):
    def __init__(self, filename, mode='r', basedir=''):
        self.filename = filename
        self.mode = mode
        if self.mode in ('w', 'a'):
            self.zfile = zipfile.ZipFile(
                filename, self.mode, compression=zipfile.ZIP_DEFLATED)
        else:
            self.zfile = zipfile.ZipFile(filename, self.mode)
        self.basedir = basedir
        if not self.basedir:
            self.basedir = os.path.dirname(filename)

    def addfile(self, path, arcname=None):
        path = path.replace('//', '/')
        if not arcname:
            if path.startswith(self.basedir):
                arcname = path[len(self.basedir):]
            else:
                arcname = ''
        self.zfile.write(path, arcname)

    def addfiles(self, paths):
        for path in paths:
            if isinstance(path, tuple):
                self.addfile(*path)
            else:
                self.addfile(path)

    def close(self):
        self.zfile.close()

    def extract_to(self, path):
        for p in self.zfile.namelist():
            self.extract(p, path)

    def extract(self, filename, path):
        if not filename.endswith('/'):
            f = os.path.join(path, filename)
            dir = os.path.dirname(f)
            if not os.path.exists(dir):
                os.makedirs(dir)
            self.zfile(f, 'wb').write(self.zfile.read(filename))
#%%
import zipfile
import csv

def kill_next(name, step):
    size = len(name)
    if(size == 0):
        return None
    id_ = (step - 1) % (size)
    res = name.pop(id_)
    yield res


# def read_zip(dirctory, mode, offset):
#     z = zipfile.ZipFile(dirctory, mode)
    
#     print(z.namelist())

#     for filename in z.namelist(  ):
#         print (filename)

#     file_name = z.namelist()[offset]

#     file_suffix = file_name.split('.')[1]

#     if file_suffix == 'txt':
#         cache = []
#         read_txt = z.read(file_name)
#         read_txt.strip('\r')
#         print(read_txt)
#         # for row in read_txt:
#         #     row = row.strip('\n')   # delete '\n'
#         #     row = row.strip('\r')   
#         #     row = row.split(',')    # convert char from txt to list 
#         #     cache.append(row)
#         return cache
#     else:
#         return None
    
# cache = z.read(file_offset)
# return cache


# with open('.\data\people.txt','r') as fp:
#     read_txt = fp.readlines()
#     for row in read_txt:
#         row = row.strip('\n') # delete '\n'
#         if row == 1:
#             continue
        
#     print(read_txt)

# import csv
# with open('.\data\people.csv','r') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         print(row)

# def fun(temp):
#     for i in range(temp):
#         yield i*2
#         print("*")

# for i in fun(5):
#     print(i,',')

# #yield: 构造迭代器，返回值给i，并且在i切换时，才执行yield后面的语句
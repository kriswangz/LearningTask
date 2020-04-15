import zipfile
import csv

def read_zip(dirctory, mode, offset):
    z = zipfile.ZipFile(dirctory, mode)
    
    print(z.namelist())

    for filename in z.namelist(  ):
        print (filename)

    file_name = z.namelist()[offset]

    file_suffix = file_name.split('.')[1]

    if file_suffix == 'txt':
        cache = []
        read_txt = z.read(file_name)
        read_txt.strip('\r')
        print(read_txt)
        # for row in read_txt:
        #     row = row.strip('\n')   # delete '\n'
        #     row = row.strip('\r')   
        #     row = row.split(',')    # convert char from txt to list 
        #     cache.append(row)
        return cache
    else:
        return None
    
# cache = z.read(file_offset)
# return cache

cache = read_zip('.\data\data.zip','r',0)
print(cache)
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
# %%
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
this file is used for mySQL testing.
"""

import pymysql

# 建库和建表
con = pymysql.connect(host='localhost', user='root',
                      passwd='123456', charset='utf8')
cur = con.cursor()
# 开始建库
cur.execute("create database awesome character set utf8;")
# 使用库
cur.execute("use awesome;")
# 建表
cur.execute("create table blogs(id char(20),user_id char(20),name char(20),)character set utf8;")

# # 打开数据库连接
# db = pymysql.connect("localhost","testuser","test123","TESTDB" )
 
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()

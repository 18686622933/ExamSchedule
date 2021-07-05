#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import sqlite3


# 在当前目录下创建数据库文件，sqlite是轻量级数据库，数据以单个文件方式保存


class SaveData:
    def __init__(self):
        self.conn = sqlite3.connect("./SData.db")
        self.cursor = self.conn.cursor()

    def createTable(self, table_name, columns):
        pass

    def insertData(self):
        pass

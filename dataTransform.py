#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import config
import pandas

df = pandas.DataFrame(config.course['data'], columns=config.course['titles'])
pandas.set_option('display.max_columns', 1000)  # 设置显示最大列数，超过会显示省略号
pandas.set_option('display.max_rows', 5000)  # 设置显示最大行数，超过会显示省略号
pandas.set_option('display.width', 1000)  # 设置每行显示的最大宽度，超过会换行
pandas.set_option('display.unicode.east_asian_width', True)  # 列明对其
# print(df)



# print(df.loc[2, '考试时间'])
a = df.loc[0]
print(a)
# print(a['考试日期'])
# print(a['考试时间'])
# print(a['年级'])

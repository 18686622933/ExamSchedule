#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import config
from myFunction import *


class TimeTransform:
    def __init__(self, exam_week):
        self.one = '8:00-10:00'
        self.two = '10:20-12:20'
        self.three = '13:30-15:30'
        self.four = '15:50-17:50'
        self.starting, self.ending = exam_week.split('-')
        self.start_year, self.end_year = [i[:4] for i in (self.starting, self.ending)]

    def getExamDays(self):
        """
        获取考试周的全部日期列表
        其中要判断考试周是否跨年
        :return:
        """
        if self.start_year == self.end_year:
            year_days = YearDays().getAllDayPerYear(self.start_year)
            start_idx = year_days.index(self.starting)
            end_idx = year_days.index(self.ending)
            res = year_days[start_idx:end_idx + 1]

        else:
            last = YearDays().getAllDayPerYear(self.start_year)
            follow = YearDays().getAllDayPerYear(self.end_year)
            start_idx = last.index(self.starting)
            end_idx = follow.index(self.ending)
            res = last[start_idx:] + follow[:end_idx + 1]

        return res

    def getNumbersOfDays(self):
        """获得考试周总天数"""
        return len(self.getExamDays())


if __name__ == '__main__':
    ts = TimeTransform(config.exam_week)
    print(ts.getExamDays())
    print(ts.getNumbersOfDays())

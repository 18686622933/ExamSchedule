#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import config
from myFunction import *


class TimeSchedule:
    def __init__(self, exam_week, max_classes):
        self.one = '8:00-10:00'
        self.two = '10:20-12:20'
        self.three = '13:30-15:30'
        self.four = '15:50-17:50'
        self.starting, self.ending = exam_week.split('-')
        self.start_year, self.end_year = [i[:4] for i in (self.starting, self.ending)]
        self.max_classes = max_classes

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
        return len(self.getExamDays())

    def getTimeForm(self):
        numbers_of_days = self.getNumbersOfDays()
        res = {}
        for i in range(1, numbers_of_days + 1):
            res[i] = {j: [] for j in range(1, 5)}

        return res

    def oneStep(self, course_data):
        day = course_data['考试日期']
        time = course_data['考试时间']
        classes = [i for i in range(1, course_data['班级数'] + 1)]
        # if day and time:
        #     self.time_form[day][time] =

    def timeSchedule(self):
        pass


if __name__ == '__main__':
    ts = TimeSchedule(config.exam_week, config.max_classes_same_time)
    print(ts.getExamDays())
    print(ts.getNumbersOfDays())
    print(ts.getTimeForm())

#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import arrow


class YearDays:
    @staticmethod
    def isLeapYear(years):
        """
        通过判断闰年，获取年份years下一年的总天数
        :param years: 年份，int
        :return:days_sum，一年的总天数
        """
        # 断言：年份不为整数时，抛出异常。
        assert isinstance(years, int), "请输入整数年，如 2018"

        if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):  # 判断是否是闰年
            # print(years, "是闰年")
            days_sum = 366
            return days_sum
        else:
            # print(years, '不是闰年')
            days_sum = 365
            return days_sum

    def getAllDayPerYear(self, years):
        """
        获取一年的所有日期
        :param years:年份
        :return:全部日期列表
        """
        start_date = '%s-1-1' % years
        a = 0
        all_date_list = []
        days_sum = self.isLeapYear(int(years))
        print()
        while a < days_sum:
            b = arrow.get(start_date).shift(days=a).format("YYYY年M月D日")
            a += 1
            all_date_list.append(b)
        # print(all_date_list)
        return all_date_list


if __name__ == '__main__':
    all_days = YearDays().getAllDayPerYear("2000")
    print(all_days)
    print(all_days.index('2000年1月1日'))
#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import copy
import config


class BackTracking:
    def __init__(self, row, courses):
        self.row = row
        self.col = len(courses)
        self.courses = courses

        self.one_result = [[0 for _ in range(self.col)] for _ in range(self.row)]  # 解是一个二维数组，纵向为时间点，横向为科目，每个节点取值为[1,0]
        self.all_result = []
        self.is_found = False  # 只需要单个解时使用

    def conflict(self, row, col):

        before_col = [i[col] for i in self.one_result][:row + 1]  # 当前课程所在纵轴上的值，取到当前行
        before_row = self.one_result[row][:col + 1]  # 当前课程所在横轴上的值，取到当前列

        # 超排
        if sum(before_col) > 1:
            return True

        # 少排
        if not sum(before_col) and row == self.row - 1:
            return True

        # 班级查重
        classes = sum([self.courses[i][1] for i in range(len(before_row)) if before_row[i]], [])
        if len(classes) > len(set(classes)):
            return True

        # 同时发生场次限制
        if sum(self.courses[i][3] for i in range(len(before_row)) if before_row[i]) > 130:
            return True

        # 毛概、大学英语、史纲、计算机时间已确定
        if row == 0 and col == self.col - 1 and not self.one_result[row][col]:
            return True

        if row == 4 and col == 14 and not self.one_result[row][col]:
            return True

        if row == 2 and col == 1 and not self.one_result[row][col]:
            return True

        if row == 7 and col == 2 and not self.one_result[row][col]:
            return True

        return False

    def backTracking(self, row, col):

        # 如要求全部解，则将本条件注销
        if self.is_found:
            return

        # 找到一个解，打印并存入all_result
        if row == self.row:
            print('got one result: %s ' % self.one_result)

            self.all_result.append(copy.deepcopy(self.one_result))
            self.is_found = True

        else:
            for boo in [1, 0]:
                self.one_result[row][col] = boo

                if not self.conflict(row, col):
                    n_col = [col + 1, 0][col + 1 == self.col]
                    n_row = [row, row + 1][col + 1 == self.col]  # 列达到最大值后换行
                    self.backTracking(n_row, n_col)

    def pprint(self, idx):
        if not self.all_result:
            print("未找到解")

        else:
            data = self.all_result[idx]
            row = len(data)
            column = len(data[0])

            for r in range(row):
                print('\n 时间 %d ：' % (r + 1), end=' ')
                for c in range(column):
                    if data[r][c]:
                        print(self.courses[c][0], len(self.courses[c][1]), end=';  ')


if __name__ == '__main__':
    BT = BackTracking(16, config.courses)
    BT.backTracking(0, 0)
    BT.pprint(0)

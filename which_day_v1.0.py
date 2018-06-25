"""
    作者：wcz
    版本：v1.0
    日期：2018/06/25
    功能：输入日期，判断第几天
"""

from datetime import datetime


def main():
    input_date_str = input('请输入日期(YYYY/mm/dd):')
    input_date = datetime.strptime(input_date_str, format('%Y/%m/%d'))

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 计算之前每月的天数以及当前月份天数综合
    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = days_in_month_tup[:month-1]
    days = sum(days) + day

    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        if month > 2:
            days += 1

    print('这是第{}天'. format(days))


if __name__ == '__main__':
    main()
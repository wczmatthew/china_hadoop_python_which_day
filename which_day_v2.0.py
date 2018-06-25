"""
    作者：wcz
    版本：v2.0
    日期：2018/06/25
    功能：用列表替换元组，输入日期，判断第几天
"""

from datetime import datetime


def is_leap_year(year):
    """
        判断year是否是闰年
    """
    is_leap = False
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        is_leap = True

    return is_leap


def main():
    input_date_str = input('请输入日期(YYYY/mm/dd):')
    input_date = datetime.strptime(input_date_str, format('%Y/%m/%d'))

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 计算之前每月的天数以及当前月份天数综合
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month_list[1] = 29

    days = days_in_month_list[:month-1]
    days = sum(days) + day

    print("这是{}年的第{}天".format(year,days))


if __name__ == '__main__':
    main()
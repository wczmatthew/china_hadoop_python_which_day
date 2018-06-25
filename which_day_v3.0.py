"""
    作者：wcz
    版本：v3.0
    日期：2018/06/25
    功能：使用集合，输入日期，判断第几天
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

    days = day
    # 包含30天的集合
    _30_days_month_set = {4, 6, 9,11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    for i in range(1, month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else:
            days += 28

    if is_leap_year(year) and month > 2:
        days += 1

    print("这是{}年的第{}天".format(year,days))


if __name__ == '__main__':
    main()
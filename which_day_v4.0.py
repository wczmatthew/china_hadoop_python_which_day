"""
    作者：wcz
    版本：v3.0
    日期：2018/06/25
    功能：使用字典，输入日期，判断第几天
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

    # 月份-天数 字典
    month_day_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    for i in range(1, month):
        days += month_day_dict[i]

    if is_leap_year(year) and month > 2:
        days += 1

    print("这是{}年的第{}天".format(year,days))


if __name__ == '__main__':
    main()
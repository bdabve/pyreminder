#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =========================================
#  FILE     : ummalqura.txt
#  CREATED  : 10-août-2020
#  AUTHOR   : daBve, dabve@outlook.fr
#  DESC     : ummalqura hijri dates
#  USAGE    : ./ummalqura.txt
# =========================================

from terminaltables import AsciiTable


def main():
    title = ' ummalqura Module '

    basic_usage = """>> from ummalqura.hijri_date import HijriDate
>> from datetime import date

>> um = HijriDate(2017, 12, 26, gr=True)               # create the object with Gregorian date

>> print('hijri month: ', um.month)                    # 4
>> print('hijri year: ', um.year)                      # 1439
>> print('arabic day name: ', um.day_name)             # الثلاثاء
>> print('arabic hijri month name: ', um.month_name)   # ربيع الثاني

>> print('english day name: ', um.day_name_en)                 # Tuesday
>> print('english gregorian month name: ', um.month_name_gr)   # December
>> print('gregorian year: ', um.year_gr)                       # 2017
>> print('gregorian month: ', um.month_gr)                     # 12
>> print('gregorian day: ', um.day_gr)                         # 26

>> print('current_month: ', HijriDate.current_month())  # 4

# the gregorian date corresponding to the first day of the given hijri month/year
>>     print('first day: ', HijriDate.month_start_date(4))             # 2017-12-19
>>     print('first day: ', HijriDate.month_start_date(4, 1439))       # 2017-12-19
>>
# the gregorian date corresponding to the last day of the given hijri month/year
>>     print('last day: ', HijriDate.month_end_date(4))            # 2018-01-17
>>     print('last day: ', HijriDate.month_end_date(4, 1439))      # 2018-01-17
>>
# Convert from gr date
>>     print('hijri month: ', HijriDate.hijri_month_from_date(date.today()))  # 4
>>     print('hijri year: ', HijriDate.hijri_year_from_date(date.today()))  # 1439
>>     print('hijri date: ', HijriDate.get_hijri_date(date.today()))  # 1439-04-08
>>     print('georing date: ', HijriDate.get_georing_date('1439-04-08'))  # 2017-12-26
    """
    # --------------------------------------------------------------------
    # main table data

    table_data = [

        ['Basic Usage', basic_usage],
    ]
    table = AsciiTable(table_data, title)
    table.inner_heading_row_border = False
    table.inner_row_border = True
    return table.table


def generate_content(func):
    """
    Generate Souce
    - This should yield prompt_toolkit `(style_string, text)` tuples.
    """
    content = func()
    for line in content:
        yield [('', line)]


if __name__ == '__main__':
    from pypager.source import GeneratorSource
    from pypager.pager import Pager

    p = Pager()                                         # create the pager
    source = GeneratorSource(generate_content(main))    # generate the source
    p.add_source(source)                                # add the content to the Pager
    p.run()

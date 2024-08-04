#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Fall 2023
Program: assignment1.py 
The python code in this file is original work written by
Taranjeet Kaur. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Taranjeet Kaur
Description: Date manipulation and validation program
'''

import sys
from datetime import datetime, timedelta

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year"
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        return 31

def after(date: str) -> str:
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    date_obj = datetime(year, mon, day)
    next_date = date_obj + timedelta(days=1)
    return next_date.strftime('%d/%m/%Y')

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, month, year = (int(x) for x in date.split('/'))
    date_obj = datetime(year, month, day)
    previous_date = date_obj - timedelta(days=1)
    return previous_date.strftime('%d/%m/%Y')

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "Check validity of date"
    try:
        day, month, year = map(int, date.split('/'))
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def day_iter(start_date: str, num: int) -> str:
    "Iterates from start date by num to return end date in DD/MM/YYYY"
    day, month, year = map(int, start_date.split('/'))
    date = datetime(year, month, day)
    end_date = date + timedelta(days=num)
    return end_date.strftime('%d/%m/%Y')

if __name__ == "__main__":
    # Check length of arguments
    if len(sys.argv) != 3:
        usage()
    
    start_date = sys.argv[1]
    num_days = sys.argv[2]

    # Check first arg is a valid date
    if not valid_date(start_date):
        usage()

    # Check that second arg is a valid number (+/-)
    if not num_days.lstrip('-').isdigit():
        usage()
    num_days = int(num_days)

    # Call day_iter function to get end date
    end_date = day_iter(start_date, num_days)

    # Print the end date
    print(f'The end date is {day_of_week(end_date)}, {end_date}.')

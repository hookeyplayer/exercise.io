# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 00:39:36 2020

@author: xiaofan
"""
from datetime import datetime
class Time:
    '''attributes:hour, minute, second'''
# =============================================================================
# 一部电影的时间报告
# =============================================================================
#%%
def print_time(t):
    print('%.2d: %.2d: %.2d' % (t.hour, t.minute, t.second))
    
# 等价于class Time里面写
#    def __str__(self):
#        return '%.2d: %.2d: %.2d' % (t.hour, t.minute, t.second)
#%%
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
#%%
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
#%%
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return false
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

#%%
# =============================================================================
# asset 作用
# if not expression:
#     raise AssertionError
# =============================================================================
def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
# 等价于class Time里面写
#    def __add__(self, other):
#        seconds = self.time_to_int() + other.time_to_int()
#        return int_to_time(seconds)
print(start + duration) # 用加号provoke__add__
#%%
def main():
    staaart = Time()
    staaart.hour = 12
    staaart.minute = 0
    staaart.second = 0
    
    print('Noon time starts at', end = ' ')
    print_time(staaart)
    
    movie = 109 # duration
    run_time = int_to_time(movie * 60) # 化为秒录入参数
    print('Duration time', end = ' ')
    print_time(run_time)
    
    end_time = add_time(staaart, run_time)
    print('Ends at', end = ' ')
    print_time(end_time)
#%%
if __name__ == '__main__':
    main()

#%%
def is_after(t1, t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def increment(t1, seconds):
    """Adds seconds to a Time object."""
    assert valid_time(t1)
    seconds += time_to_int(t1)
    return int_to_time(seconds)


def mul_time(t1, factor):
    """Multiplies a Time object by a factor."""
    assert valid_time(t1)
    seconds = time_to_int(t1) * factor
    return int_to_time(seconds)
#%%
def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
    # when is my birthday this year?
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # if it has gone by, when will it be next year
    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)

    # subtraction on datetime objects returns a timedelta object
    delta = next_birthday - today
    return delta.days


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.
    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    dday = b1 + delta
    return dday


def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week
    today = datetime.today()
    print(today.weekday())
    print(today.strftime('%A'))

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1967, 5, 2)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2006, 12, 26)
    b2 = datetime(2003, 10, 11)
    print('Double Day', end=' ')
    print(double_day(b1, b2))


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print('Starts at', end=' ')
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print('Run time', end=' ')
    print_time(run_time)

    # what time does the movie end?
    end_time = add_times(noon_time, run_time)
    print('Ends at', end=' ')
    print_time(end_time)

    print('Does it end after it begins?', end=' ')
    print(is_after(end_time, noon_time))

    print('Home by', end=' ')
    travel_time = 600      # 10 minutes
    home_time = increment(end_time, travel_time)
    print_time(home_time)

    race_time = Time()
    race_time.hour = 1
    race_time.minute = 34
    race_time.second = 5

    print('Half marathon time', end=' ')
    print_time(race_time)

    distance = 13.1       # miles
    pace = mul_time(race_time, 1/distance)

    print('Time per mile', end=' ')
    print_time(pace)

    datetime_exercises()


if __name__ == '__main__':
    main()
    

    

import datetime as dt

def solution(a, b):
    answer = dt.datetime(2016, a, b)
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return days[answer.weekday()]
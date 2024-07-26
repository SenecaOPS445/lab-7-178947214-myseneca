#!/usr/bin/env python3
# Student ID: 178947214
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    # Check for seconds overflow and carry over to minutes
    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second = sum.second % 60

    # Check for minutes overflow and carry over to hours
    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute = sum.minute % 60
    
    # Check for negative seconds and borrow from minutes
    while sum.second < 0:
        sum.minute -= 1
        sum.second += 60

    # Check for negative minutes and borrow from hours
    while sum.minute < 0:
        sum.hour -= 1
        sum.minute += 60

    return sum

def valid_time(t):
    """Check for the validity of the time object attributes:
       24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):
    """Add or subtract seconds from the time object and handle overflow/underflow."""
    # Update the seconds
    time.second += seconds
    
    # Handle overflow/underflow for seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
        
    while time.second < 0:
        time.second += 60
        time.minute -= 1
        
    # Handle overflow/underflow for minutes
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
        
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
        
    # Handle hours if needed (although it's not specified to handle hours in this function, it's good to check)
    if time.hour < 0:
        time.hour = 0
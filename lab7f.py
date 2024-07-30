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

    def __str__(self):
        """Return a user-friendly string representation of the Time object."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a detailed string representation of the Time object."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, other):
        """Add two Time objects and return a new Time object."""
        if not isinstance(other, Time):
            return NotImplemented
        
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return sec_to_time(total_seconds)

    def format_time(self):
        """Return time object as a formatted string"""
        return self.__str__()

    def sum_times(self, other):
        """Add this time object with another time object and return the sum."""
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Add or subtract seconds from this time object and handle overflow/underflow."""
        # Convert current time to total seconds
        total_seconds = self.time_to_sec() + seconds
        
        # Convert total seconds back to a Time object
        new_time = sec_to_time(total_seconds)
        
        # Update this object's attributes
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second

        return self

    def time_to_sec(self):
        """Convert this Time object to seconds"""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check for the validity of the time object attributes:
           24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert seconds to a Time object"""
    # Handle negative seconds if necessary
    seconds %= 86400  # Total seconds in a day
    
    hours = (seconds // 3600) % 24
    seconds %= 3600
    minutes = (seconds // 60) % 60
    seconds %= 60
    return Time(hours, minutes, seconds)

"""
Create a class called TimeUtils that has a static method called time_to_seconds 
that takes a time string in the format hh:mm:ss and returns the total number of seconds represented by that time. 
Use functional programing paradigm.
"""

class TimeUtils:

    @staticmethod
    def time_to_seconds(time: str) -> str:
        splited_time = time.split(":")
        hours_to_seconds = (lambda x: x*3600) (int(splited_time[0]))
        minutes_to_seconds = (lambda x: x*60) (int(splited_time[1]))
        time_to_seconds = hours_to_seconds + minutes_to_seconds + int(splited_time[2])
        return f'Time {time} is equel: {time_to_seconds}s'

print(TimeUtils.time_to_seconds(time = "05:00:00"))




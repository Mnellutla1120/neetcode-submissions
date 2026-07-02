"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
     #first sort the list by start times
     intervals.sort(key=lambda x: x.start)

     '''
     does the end time of the previous meeting conflict 
     w the start time of the next one?
     '''
     for i in range(len(intervals)-1):
        if intervals[i+1].start < intervals[i].end:
            return False
     return True

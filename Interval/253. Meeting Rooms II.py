'''
Question
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example, Given [[0, 30],[5, 10],[15, 20]], return 2.

Thinking:
Method 1:

Sort the intervals according to the starting time.
Use a minHeap(pq) to save the endTime for all intervals according to the order of start time.
Add end time to the pq.
if cur start time < pq.peek() => means current start time is before first ending time, which means we must have a new room.
if cur start time >= pq.peek() => means we can use this room for the meeting, we poll out the the original period and add current period to the pq(Means we update the room with the new meeting).
'''
'''
Greedy: We need to wrap the end time of interval as one room and append it to rooms. 
First we sort the interval. Then we iterate the given interval, if the current interval’s start time is bigger or equal than any room’s end time in rooms, 
we will append the current interval’s end time to this room; if the current interval’s start time is not bigger or not equal than any room’s end time in rooms, 
we will wrap this end time of the current interval as one room and append it to rooms. Finally, the result will be the size of the rooms.
'''
from typing import List
def minMeetingRooms(intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size<=1: return size
        sorted_intervals = sorted(intervals)
        rooms=[[sorted_intervals[0][1]]]
        for i in range(1,size):
            booked = False
            for room in rooms:
                if sorted_intervals[i][0]>=room[-1]:
                    room.append(sorted_intervals[i][1])
                    booked = True
                    break
            if not booked:rooms.append([sorted_intervals[i][1]])
        return len(rooms)

print(minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(minMeetingRooms([[7,10],[2,4]]))
print(minMeetingRooms([[1,6], [2,5], [10,14]]))


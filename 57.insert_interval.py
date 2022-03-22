"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
from re import T
from typing import List
from collections import deque

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and not newInterval:
            return None
        intervals.append(newInterval)
        intervals.sort()

        merged = [intervals[0]]
        for i in intervals[1:]:            
            if i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)
        
        return merged
        
        
        

# print(insert([[1,3],[6,9]], [2,5]))
# print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(insert([], [4,8]))
"""
4. Median of Two Sorted Arrays
Hard

13899

1791

Add to List

Share
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        #1. merge both
        #2. sort
        #3. get midpoint
        #4. get median
        #5. return median
       
        
        #1. merge both
        nums1 = nums1 + nums2

        #2.sort
        nums1.sort()

        #3. get midpoint
        mid = len(nums1) // 2

        #4. get median
        res = (nums1[mid] + nums1[~mid]) / 2

        #5. return median
        return res

        
        
print(findMedianSortedArrays([], [1]))
print(findMedianSortedArrays([], [2]))
print(findMedianSortedArrays([1], [1]))
print(findMedianSortedArrays([3], [-2, -1]))
print(findMedianSortedArrays([2,2,4,4],[2,2,4,4]))
print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))
print(findMedianSortedArrays([1,2], [3,4,5]))
print(findMedianSortedArrays([1,2,3], [4,5,6]))
print(findMedianSortedArrays([1,2,3,4], [5,6,7,8]))
print(findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10]))
print(findMedianSortedArrays([1,2,3,4,5,6], [7,8,9,10,11,12]))
print(findMedianSortedArrays([1,2,3,4,5,6,7], [8,9,10,11,12,13,14]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8], [9,10,11,12,13,14,15,16]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9], [10,11,12,13,14,15,16,17,18]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11], [12,13,14,15,16,17,18,19,20,21,22]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12], [13,14,15,16,17,18,19,20,21,22,23,24]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13], [14,15,16,17,18,19,20,21,22,23,24,25,26]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14], [15,16,17,18,19,20,21,22,23,24,25,26,27,28]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]))
            
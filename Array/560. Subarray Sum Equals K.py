"""
560. Subarray Sum Equals K
Medium

10405

342

Add to List

Share
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    count = sum = 0
    maps = dict()
    for n in nums:
        sum += n

        if sum == k:
            count  += 1
        if (sum - k) in maps:
            count += maps[sum - k]
        if sum in maps:
            maps[sum] += 1
        else:
            maps[sum] = 1
    return count



# print(subarraySum([1,1,1], 2))
print(subarraySum([1,2,3], 3))

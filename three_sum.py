"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
        if len(nums) < 1:
            return list()
        n = list()

        k = len(nums)
        nums.sort()

        for i in range(0, k):
          start = i + 1
          end = k - 1
          res = 0-nums[i]

          while start < end:
            if nums[i]+nums[start]+nums[end]==0 and [nums[i],nums[start],nums[end]] not in n:
                n.append([nums[i],nums[start],nums[end]])
                start+=1
                end-=1
            elif nums[start]+nums[end] > res:
                end-=1
            else:
                start+=1
          
        return n

print(threeSum([-1,0,1,2,-1,-4]))

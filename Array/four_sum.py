"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
        res = list()
        
        if not nums:
            return res
        
        if len(nums) < 4:
            return res.append(nums)
        
        nums.sort()
        
        for i in range(len(nums) - 3):
            
            for j in range(i + 1, len(nums) - 2):
                
                suma = nums[i] + nums[j]
                left = j + 1
                right = len(nums) - 1
                
                while left< right:
                    sumb = suma + nums[right] + nums[left]
                    if sumb == target:
                        if [nums[i] , nums[j], nums[right] , nums[left]] not in res:
                            res.append([nums[i] , nums[j], nums[right] , nums[left]])
                        left += 1
                        right -= 1
                    elif sumb < target:
                        left += 1
                    else:
                        right -=1
        return res

print(fourSum([1,0,-1,0,-2,2], 0))
print(fourSum([2,2,2,2,2], 8))
print(fourSum([-1,0,1,2,-1,-4], -1))
print(fourSum([0,0,0,0,0], 0))
print(fourSum([-1,0,1,2,-1,-4], -1))
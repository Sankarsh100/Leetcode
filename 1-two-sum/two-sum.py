from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                       # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:      # found the pair
                return [seen[complement], i]
            seen[num] = i               # save this number’s index
        # By problem statement a solution always exists,
        # so we never reach this line.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i, j in enumerate(nums):
            map[j] = i

        for i in range(len(nums)):
            if target - nums[i] in map:
                return [i, map[target-nums[i]]]



            
       
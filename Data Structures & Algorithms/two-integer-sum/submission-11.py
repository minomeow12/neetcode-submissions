class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = i
        
        for i in range(len(nums)):
            find = target - nums[i]
            if find in maps:
                return [i, maps[find]]
                
            



            
       
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i, j in enumerate(nums):
            map[j] = i

        for i in range(len(nums)):
            j = target - nums[i]
            if j in map:
                if j != i and map[j] != i:
                    return sorted([i,map[j]])



            
       
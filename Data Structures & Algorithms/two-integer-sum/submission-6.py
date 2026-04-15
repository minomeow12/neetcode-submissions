class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(len(nums)):
        #    for j in range(i+1, len(nums)):
        #        if nums[i] + nums[j] == target:
        #          return [i,j]

        map = {}

        for i,val in enumerate(nums):
            map[val] = i

        for i,n in enumerate(nums):
            diff = target - n
            if diff in map and map[diff] != i:
                if i < map[diff]:
                    return [i, map[diff]]
                else:
                    return [map[diff], i]
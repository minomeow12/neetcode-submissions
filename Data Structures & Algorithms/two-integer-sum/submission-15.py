class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, j in enumerate(nums):
            map[j] = i
        
        for i in map:
            found = target - i
            if found in map and map[i] != map[found]:
                return [map[i], map[found]]
        return []
        #time: O(n), space: O(n) + O(1)

    

                
        
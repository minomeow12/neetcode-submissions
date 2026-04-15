class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for i in nums:
            map[i] = 1 + map.get(nums[i], 0)

        for i in map:
            if map[i] >= k:
                return nums[i]

        return []
        
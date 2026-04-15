class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        a= []

        for i in nums:
            map[i] = 1 + map.get(i, 0)

        for i in map:
            if map[i] >= k:
                a.append(i)

        return a
                
        
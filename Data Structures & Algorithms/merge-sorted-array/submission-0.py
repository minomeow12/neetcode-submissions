class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #m: number of elements to be merged
        #n: placeholder, element in num2
        #edge case:
        if m == 0:
            nums1[:] = nums2

        else:
            j = 0
            for i in range(m, len(nums1)):
                nums1[i] = nums2[j]
                j += 1

        nums1.sort();
                
        
        
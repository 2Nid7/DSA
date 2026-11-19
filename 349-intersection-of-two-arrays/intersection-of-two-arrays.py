class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n1=set(nums1)
        n2=set(nums2)
        k=n1.intersection(n2)
        return list(k)
        
        
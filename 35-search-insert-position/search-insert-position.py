class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        s=0
        e=len(nums)-1
        mid=s+(e-s)//2
        while s<=e:
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                s=mid+1
            elif nums[mid]>target:
                e=mid-1
            mid=s+(e-s)//2
            
        return s


        
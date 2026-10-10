class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ans=-1
        s=0
        e=len(nums)-1
        mid=s+(e-s)//2
        while s<=e:
            if nums[mid]==target:
                ans=mid
                return ans
            if nums[mid]<target:
                s=mid+1
            else:
                e=mid-1
            mid=s+(e-s)//2
        return ans
        
        
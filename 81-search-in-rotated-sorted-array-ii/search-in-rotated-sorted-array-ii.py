class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        s=0
        k=target
        e=len(nums)-1
        mid=s+(e-s)//2
        while s<=e:
            if nums[mid]==k:
                return True
            elif nums[s]==nums[mid]==nums[e]:
                s=s+1
                e-=1
            elif nums[s]<=nums[mid]:
                if nums[s]<=k<nums[mid]:
                    e=mid-1
                else:
                    s=mid+1
            else:
                if nums[mid]<k<=nums[e]:
                    s=mid+1
                else:
                    e=mid-1
            mid=s+(e-s)//2
        else:
            return False
        
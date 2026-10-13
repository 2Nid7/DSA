class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums)==0:
            return [-1,-1]

        def first(nums,target):
            s=0
            e=len(nums)-1
            mid=s+(e-s)//2
            ans=-1
            while s<=e:
                if nums[mid]==target:
                    ans=mid
                    e=mid-1
                elif nums[mid]<target:
                    s=mid+1
                elif nums[mid]>target:
                    e=mid-1
                mid=s+(e-s)//2
            return ans
        def last(nums,target):
            s=0
            e=len(nums)-1
            mid=s+(e-s)//2
            ans=-1
            while s<=e:
                if nums[mid]==target:
                    ans=mid
                    s=mid+1
                elif nums[mid]<target:
                    s=mid+1
                elif nums[mid]>target:
                    e=mid-1
                mid=s+(e-s)//2
            return ans

        firs=first(nums,target)
        la=last(nums,target)
        return [firs,la]

        # def last(nums,target,ans):
        #     s=0
        #     e=len(nums)-1
        #     mid=s+(e-s)//2
        #     ans2=-1
        #     while s<=e:
        #         if nums[mid]==target:
        #             ans=mid
        #             s=mid+1
        #         elif nums[mid]<target:
        #             s=mid+1
        #         elif nums[mid]>target:
        #             e=mid-1
        #         mid=s+(e-s)//2
        #     return [ans,ans2]

        # def firstoccurence(nums,target):
        #     s=0
        #     e=len(nums)-1
        #     mid=s+(e-s)//2
        #     ans=-1
        #     while s<=e:
        #         if nums[mid]==target:
        #             ans=mid
        #             e=mid-1
        #         elif nums[mid]<target:
        #             s=mid+1
        #         elif nums[mid]>target:
        #             e=mid-1
        #         mid=s+(e-s)//2
        #     return last(nums,target,ans)
        # return firstoccurence(nums,target)


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        s=1
        e=max(piles)
        mid=s+(e-s)//2
        ans=-1
        while s<=e:
            sum=0
            for i in range(len(piles)):
                sum=sum+(math.ceil(piles[i]/mid))
            if sum>h:
                s=mid+1
            else:
                ans=mid
                e=mid-1
            mid=s+(e-s)//2
        return ans


        


        
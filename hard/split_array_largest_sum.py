'''
Split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.
Return the largest sum among these subarrays.
'''
class Solution(object):
    def splitArray(self, nums, m):
        high=sum(nums)
        low=max(nums)
        mid=(high+low)//2
        while(mid!=low):
            if self.Isvalid(nums,m,mid):
                high=mid
            else:
                low=mid+1
            mid=(high+low)//2
        if self.Isvalid(nums,m,mid):
            return mid
        else:
            return mid+1
            
    def Isvalid(self,nums,m,mid):
        total=0
        for i in range(len(nums)):
            if total+nums[i]>mid:
                m=m-1
                total=0
            if m<1:
                return False
            total+=nums[i]
        return True


def searchInsert(nums, target):
        if target>nums[-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        m=0
        n=len(nums)-1
        
        while((n-m)!=1):
            x=int((m+n)/2)
            if nums[x]==target:
                return x
            elif nums[x]>target:
                n=x
            else:
                m=x
        if nums[m]==target:
            return m
        return n
class Solution(object):
    def maxProduct(self, nums):
        curr_max=nums[0]
        curr_min=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            temp=curr_max
            curr_max=max(num,curr_max*num,curr_min*num)
            curr_min=min(num,temp*num,curr_min*num)
            ans=max(ans,curr_max)
        return ans
       
                
                
               
                
        
        
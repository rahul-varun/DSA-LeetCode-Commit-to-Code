class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res=0
        for i in range(len(nums)):
            if nums[i] !=0:
                temp=nums[i]
                nums[i]=0
                nums[res]=temp
                res +=1

                
        
        
        
        

        
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False

        #approch 2.: using set
        # temp=set()
        # for i in nums:
        #     if i in temp:
        #         return True
        #     temp.add(i)
        
        # return False
        